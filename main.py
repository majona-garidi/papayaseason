import sys
import json
import calendar
import os
import typing

from datetime import date

from PyQt5 import QtCore

from PyQt5.QtGui import QPixmap, QMovie, QCursor, QFont, QFontDatabase

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout


# We need absolute path so the font file can be found in users directory
# font file needs to be in same directory as main.py
root_dir = os.path.dirname(os.path.abspath(__file__))

widgets = {

    "logo": [],
    "logo_small": [],
    "start_button": [],
    "button": [],
    "question": [],
    "answers": [],
    "result": [],
    "animation": [],
    "header": [],
    "description": [],
    "back": [],
}


app = QApplication(sys.argv)


grid = QGridLayout()


def create_window(title, minimum_width, minimum_height):

    window = QWidget()
    window.setWindowTitle(title)
    window.adjustSize()
    window.setMinimumSize(minimum_width, minimum_height)
    window.setStyleSheet(
        "background: '#F2CEE8'"
        )

    return window


def load_font(font_file_name):

    path_to_font_file = os.path.join(root_dir, font_file_name)
    id = QFontDatabase.addApplicationFont(path_to_font_file)

    if id < 0:

        print(f"Font file {path_to_font_file} not found")

    font_families = QFontDatabase.applicationFontFamilies(id)
    font_name = font_families[0]

    return QFont(font_name)


clicked_country = None


def clear_widgets():

    for widget in widgets:

        if widgets[widget] != []:

            widgets[widget][-1].hide()

            for w in widgets[widget]:

                w.hide()

        for i in range(0, len(widgets[widget])):

            widgets[widget].pop()


def get_countries_list_from_json(data_file_name):

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


def get_main_season_list_from_clicked_button():

    with open("seasons.json", "r") as f:

        data = json.load(f)

    for country_dict in data["countries"]:

        if country_dict["country"] == clicked_country:

            main_season_list = country_dict["mainSeason"]

            return main_season_list


def main_season_list_as_months():

    month_list = []

    for i in get_main_season_list_from_clicked_button():

        monat = calendar.month_name[i]

        month_list.append(monat)

    return month_list


current_month = None


def next_papaya_season():

    # supposing that value at index 0 in the json data has also the lowest value of all entries
    next_season_start = main_season_list_as_months()[0]

    return next_season_start


def end_of_papaya_season():

    # supposing that value at index 0 in the json data has also the lowest value of all entries
    end_of_season = main_season_list_as_months()[-1]

    return end_of_season


def get_availability_list_from_clicked_button():

    with open("seasons.json", "r") as f:
        data = json.load(f)

    for country_dict in data["countries"]:

        if country_dict["country"] == clicked_country:

            return country_dict["availability"]


current_month = date.today().month


def is_season():

    season_list = get_main_season_list_from_clicked_button()

    if current_month in season_list:

        return True

    else:

        return False


def answer_sentence():

    if is_season():

        return f"It's papaya season in {clicked_country}. The season ends in {end_of_papaya_season()}."
    else:

        return f"The next papaya season in {clicked_country} starts in {next_papaya_season()}."


def which_button_was_clicked(clicked_button):

    # sender() method of class QWidget saves whichever object sent a signal, here: clicked button
    global clicked_country
    clicked_country = clicked_button.sender().text()

    return clicked_country


def show_frame1():

    clear_widgets()
    frame_1()


def show_frame2():

    clear_widgets()
    frame_2()


def show_frame3():

    clear_widgets()
    frame_3()


def start_game():

    clear_widgets()
    frame_2()


def create_buttons(answer):

    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font("DidactGothic-Regular.ttf")
    button.setFont(button_font)
    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "margin-left: 100px;" +
        "margin-right: 100px;" +
        "color: #353535;" +
        "font-size: 20px;" +
        "padding: 12px 0;" +
        "margin-top: 10px}" +
        "*:hover{background-color: '#C6FF33'}"
    )

    return button


def create_logo_widget(logo_file):

    image = QPixmap(logo_file)
    logo = QLabel()
    logo.setPixmap(image)
    widgets["logo"].append(logo)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 20px;"
    )

    return logo


def create_header_widget(header_text, font_file_name):
    header = QLabel(header_text)
    font_header = load_font(font_file_name)
    header.setFont(font_header)
    widgets["header"].append(header)
    header.setAlignment(QtCore.Qt.AlignCenter)
    header.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding-top: 40px;" +
        "padding-bottom: 10px;"
        )

    return header


def create_description_widget(description_text, font_file_name):

    description = QLabel(description_text)
    widgets["description"].append(description)
    description.setAlignment(QtCore.Qt.AlignCenter)
    font_description = load_font(font_file_name)
    description.setFont(font_description)
    description.setStyleSheet(
        "font-size: 20px;" +
        "color: '#353535';"
    )

    return description


def create_start_button(start_button_text, font_file_name):
    start_button = QPushButton(start_button_text)
    start_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font(font_file_name)
    start_button.setFont(button_font)
    widgets["start_button"].append(start_button)
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


def create_question_widget(question_text, font_file_name):

    question = QLabel(question_text)
    question.setAlignment(QtCore.Qt.AlignCenter)
    question_font = load_font(font_file_name)
    question.setFont(question_font)
    widgets["question"].append(question)
    question.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 60px;"+
        "margin-top: 20px;"
    )
    return question


def fill_button_with_data(data_file_name):

    for i in range(0, number_of_countries):

        button = create_buttons(get_countries_list_from_json(data_file_name)[i])
        widgets["answers"].append(button)

        # Every new button object stores the function below
        # if the button gets clicked, the lambda function gets executed
        # connect usually only requires the name of a  normal function, not a lambda function
        # but without the lambda it wasn't possible to pass the button argument
        button.clicked.connect(lambda: which_button_was_clicked(button))

        button.clicked.connect(show_frame3)


def create_small_logo_widget():

    image = QPixmap("icons/logo_110px.png")
    logo_small = QLabel()
    logo_small.setPixmap(image)
    logo_small.setAlignment(QtCore.Qt.AlignCenter)
    logo_small.setStyleSheet(
        "margin-top: 50x;" +
        "margin-bottom: 15px;"
    )
    widgets["logo_small"].append(logo_small)

    return logo_small


def place_animation_on_grid(affirming_animation_file_name, warning_animation_file_name):

    if is_season():

        place_affirming_animation_on_grid(affirming_animation_file_name)

    else:

        place_warning_animation_on_grid(warning_animation_file_name)


def place_warning_animation_on_grid(animation_file_name):

    label = QLabel()
    animation = QMovie(animation_file_name)
    label.setMovie(animation)
    animation.start()
    widgets["animation"].append(label)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(
        "margin-top: 20px;"
    )

    grid.addWidget(widgets["animation"][-1], 0, 0, 3, 2)


def place_affirming_animation_on_grid(animation_file_name):

        label = QLabel()
        animation = QMovie(animation_file_name)
        label.setMovie(animation)
        animation.start()
        widgets["animation"].append(label)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet(
            "margin-top: 20px;"
        )

        grid.addWidget(widgets["animation"][-1], 0, 0, 3, 2)


def create_result_widget(font_file_name):

    result = QLabel(answer_sentence())
    result.setAlignment(QtCore.Qt.AlignCenter)
    result.setWordWrap(True)
    result_font = load_font(font_file_name)
    result.setFont(result_font)
    result.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 50px;"
    )
    widgets["result"].append(result)

    return result


def create_back_button(back_button_text, font_file_name):

    button = QPushButton(back_button_text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font(font_file_name)
    button.setFont(button_font)
    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "font-size: 30px;" +
        "color: '#353535';" +
        "padding: 2px 0;" +
        "margin: 85px 120px;}" +
        "*:hover{background: '#C6FF33';}"
    )
    button.clicked.connect(show_frame2)

    widgets["back"].append(button)

    return button


def frame_1():

    create_logo_widget("icons/logo_300px.png")
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)

    create_header_widget("Enjoy better papayas - go by their harvest time", "DidactGothic-Regular.ttf")
    grid.addWidget(widgets["header"][-1], 4, 0, 1, 2)

    description = (
        "Simply choose where your papaya is from and let" + "\n" +
        "the app check the harvest time of the country" + "\n" +
        "that you've chosen. Enjoy a fresher fruit."
    )
    create_description_widget(description, "DidactGothic-Regular.ttf")
    grid.addWidget(widgets["description"][-1], 5, 0, 1, 2)

    create_start_button("Start", "DidactGothic-Regular.ttf")
    grid.addWidget(widgets["start_button"][-1], 6, 0, 1, 2)


def frame_2():

    create_question_widget("Where is your papaya from?", "DidactGothic-Regular.ttf")
    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)

    fill_button_with_data("seasons.json")
    # buttons for countries start from second row in grid
    for i, j in zip(range(0, number_of_countries), range(2, number_of_countries + 2)):

        grid.addWidget(widgets["answers"][i], j, 0, 1, 2)

    create_small_logo_widget()
    # number of rows is dependent on number of countries for flexible position on grid
    grid.addWidget(widgets["logo_small"][-1], number_of_countries + 2, 0, 1, 2)


def frame_3():

    place_animation_on_grid(affirming_animation_file_name="icons/confirmation_500px.gif", warning_animation_file_name="icons/warning_500px.gif")

    create_result_widget("DidactGothic-Regular.ttf")
    grid.addWidget(widgets["result"][-1], 4, 0, 2, 2)

    create_back_button("Try another country", "DidactGothic-Regular.ttf")
    grid.addWidget(widgets["back"][-1], 5, 0, 2, 2)


window = create_window(title="Papaya Season", minimum_width=600, minimum_height=840)
window.setLayout(grid)
window.show()


frame_1()


sys.exit(app.exec())
