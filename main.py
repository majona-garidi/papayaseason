import sys
import json
import calendar
import os

import view
import model
import controller

from pathlib import Path

from typing import Union

from datetime import date

from PyQt5 import QtCore

from PyQt5.QtGui import QPixmap, QMovie, QCursor, QFont, QFontDatabase

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout


clicked_country = None


def get_countries_list_from_json(data_file_name) -> list[str]:

    with open(data_file_name, "r") as f:

        data = json.load(f)

        countries = []

        # length of list countries in json data for flexible number of countries
        for i in range(len(data["countries"])):

            countries.append(data["countries"][i]["country"])

        return countries


# TODO: global?refactor?
# TODO: strong coupling data_file_name
number_of_countries = len(get_countries_list_from_json("seasons.json"))


main_season_for_clicked_button = None


def get_main_season_list_from_clicked_button() -> list[int]:

    with open("seasons.json", "r") as f:

        data = json.load(f)

    for country_dict in data["countries"]:

        if country_dict["country"] == clicked_country:

            main_season_list = country_dict["mainSeason"]

            return main_season_list


def main_season_list_as_months() -> list[str]:

    month_list = []

    for i in get_main_season_list_from_clicked_button():

        monat = calendar.month_name[i]

        month_list.append(monat)

    return month_list


current_month = None


def next_papaya_season() -> str:

    # supposing that value at index 0 in the json data has also the lowest value of all entries
    next_season_start = main_season_list_as_months()[0]

    return next_season_start


def end_of_papaya_season() -> str:

    # supposing that value at index 0 in the json data has also the lowest value of all entries
    end_of_season = main_season_list_as_months()[-1]

    return end_of_season


current_month = date.today().month


def is_season() -> bool:

    season_list = get_main_season_list_from_clicked_button()

    if current_month in season_list:

        return True

    else:

        return False


def answer_sentence() -> str:

    if is_season():

        return f"It's papaya season in {clicked_country}. The season ends in {end_of_papaya_season()}."
    else:

        return f"The next papaya season in {clicked_country} starts in {next_papaya_season()}."


def which_button_was_clicked(clicked_button: QPushButton) -> str:

    # sender() method of class QWidget saves whichever object sent a signal, here: clicked button
    global clicked_country
    clicked_country = clicked_button.sender().text()

    return clicked_country


def create_start_button(start_button_text: str) -> QPushButton:

    start_button = QPushButton(start_button_text)
    start_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    view.widgets["start_button"].append(start_button)
    start_button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "font-size: 30px;" +
        "color: '#353535';" +
        "padding: 2px 0;" +
        "margin: 85px 160px;}" +
        "*:hover{background: '#C6FF33';}"
    )

    start_button.clicked.connect(start_game)

    return start_button

def show_frame1():

    view.clear_widgets()
    view.frame_1()


def show_frame2():

    view.clear_widgets()
    view.frame_2()


def show_frame3():

    view.clear_widgets()
    view.frame_3()


def start_game():

    view.clear_widgets()
    view.frame_2()


def frame_1():

    view.create_logo_widget("icons/logo_300px.png")
    view.grid.addWidget(view.widgets["logo"][-1], 0, 0, 1, 2)

    view.create_header_widget("Enjoy better papayas - go by their harvest time")
    view.grid.addWidget(view.widgets["header"][-1], 4, 0, 1, 2)

    description = (
        "Simply choose where your papaya is from and let" + "\n" +
        "the app check the harvest time of the country" + "\n" +
        "that you've chosen. Enjoy a fresher fruit."
    )
    view.create_description_widget(description)
    view.grid.addWidget(view.widgets["description"][-1], 5, 0, 1, 2)

    create_start_button("Start")
    view.grid.addWidget(view.widgets["start_button"][-1], 6, 0, 1, 2)


    def frame_2():
        # TODO frame_2() got imported to view because of the function fill_button_with_data() and others, but needs to use number_of_countries - delete gloabl variable number_of_countries?
        global number_of_countries

        view.create_question_widget("Where is your papaya from?")
        view.grid.addWidget(view.widgets["question"][-1], 0, 0, 1, 2)

        view.fill_button_with_data("seasons.json")
        # buttons for countries start from second row in grid
        for i, j in zip(range(0, number_of_countries), range(2, number_of_countries + 2)):
            view.grid.addWidget(view.widgets["answers"][i], j, 0, 1, 2)

        view.create_small_logo_widget()
        # number of rows is dependent on number of countries for flexible position on grid
        view.grid.addWidget(view.widgets["logo_small"][-1], number_of_countries + 2, 0, 1, 2)


    def frame_3():
        view.place_animation_on_grid(affirming_animation_file_name="icons/confirmation_500px.gif",
                                warning_animation_file_name="icons/warning_500px.gif")

        view.create_result_widget()
        view.grid.addWidget(view.widgets["result"][-1], 4, 0, 2, 2)

        view.create_back_button("Try another country")
        view.grid.addWidget(view.widgets["back"][-1], 5, 0, 2, 2)


window = view.create_window(title="Papaya Season", minimum_width=600, minimum_height=840)
window.setLayout(view.grid)
window.show()


frame_1()


sys.exit(view.app.exec())
