import sys
import json
import calendar
import os

import model
import controller

from pathlib import Path

from typing import Union

from datetime import date

from PyQt5 import QtCore

from PyQt5.QtGui import QPixmap, QMovie, QCursor, QFont, QFontDatabase

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)
grid = QGridLayout()


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

def clear_widgets():

    for widget in widgets:

        if widgets[widget] != []:

            widgets[widget][-1].hide()

            for w in widgets[widget]:

                w.hide()

        for i in range(0, len(widgets[widget])):

            widgets[widget].pop()

def create_window(title: str, minimum_width: int, minimum_height: int) -> QWidget:

    window = QWidget()
    window.setWindowTitle(title)
    window.adjustSize()
    window.setMinimumSize(minimum_width, minimum_height)
    window.setStyleSheet(
        "background: '#F2CEE8'"
        )

    return window


def create_header_widget(header_text: str) -> QLabel:
    header = QLabel(header_text)
    widgets["header"].append(header)
    header.setAlignment(QtCore.Qt.AlignCenter)
    header.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding-top: 40px;" +
        "padding-bottom: 10px;"
        )

    return header

def create_back_button(back_button_text: str) -> QPushButton:

    button = QPushButton(back_button_text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "font-size: 30px;" +
        "color: '#353535';" +
        "padding: 2px 0;" +
        "margin: 85px 120px;}" +
        "*:hover{background: '#C6FF33';}"
    )
    button.clicked.connect(main.show_frame2)

    widgets["back"].append(button)

    return button


def create_question_widget(question_text: str) -> QLabel:

    question = QLabel(question_text)
    question.setAlignment(QtCore.Qt.AlignCenter)
    widgets["question"].append(question)
    question.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 60px;" +
        "margin-top: 20px;"
    )

    return question


def fill_button_with_data(data_file_name: Union[str, Path]):
    global number_of_countries

    for i in range(0, number_of_countries):

        country = get_countries_list_from_json(data_file_name)[i]
        button = create_buttons(text_on_button=country)
        widgets["answers"].append(button)

        # Every new button object stores the function below
        # if the button gets clicked, the lambda function gets executed
        # connect usually only requires the name of a  normal function, not a lambda function
        # but without the lambda it wasn't possible to pass the button argument
        button.clicked.connect(lambda: which_button_was_clicked(button))

        button.clicked.connect(main.show_frame3)


def create_buttons(text_on_button: str) -> QPushButton:

    button = QPushButton(text_on_button)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
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


def create_logo_widget(logo_file: Union[str, Path]) -> QLabel:

    image = QPixmap(logo_file)
    logo = QLabel()
    logo.setPixmap(image)
    widgets["logo"].append(logo)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 20px;"
    )

    return logo


def create_description_widget(description_text: str) -> QLabel():

    description = QLabel(description_text)
    widgets["description"].append(description)
    description.setAlignment(QtCore.Qt.AlignCenter)
    description.setStyleSheet(
        "font-size: 20px;" +
        "color: '#353535';"
    )

    return description


def create_small_logo_widget() -> QLabel:

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


def place_animation_on_grid(affirming_animation_file_name: Union[str, Path], warning_animation_file_name: Union[str, Path]):

    if is_season():

        place_affirming_animation_on_grid(affirming_animation_file_name)

    else:

        place_warning_animation_on_grid(warning_animation_file_name)


def place_warning_animation_on_grid(animation_file_name: Union[str, Path]):

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


def place_affirming_animation_on_grid(animation_file_name: Union[str, Path]):

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


def create_result_widget() -> QLabel:

    result = QLabel(answer_sentence())
    result.setAlignment(QtCore.Qt.AlignCenter)
    result.setWordWrap(True)
    result.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 50px;"
    )
    widgets["result"].append(result)

    return result







