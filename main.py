import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import json

from datetime import date


widgets = {

    "logo": [],
    "button": [],
    "question": [],
    "answers": []

}

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Papaya Season")
window.setFixedWidth(1000)
# window.move(2700, 200)
window.setStyleSheet("background: 'white'")

grid = QGridLayout()


def clear_widgets():

    for widget in widgets:

        if widgets[widget] != []:

            widgets[widget][-1].hide()

            for w in widgets[widget]:

                w.hide()

        for i in range(0, len(widgets[widget])):

            widgets[widget].pop()


def get_countries_list_from_json():

    with open("seasons.json", "r") as f:

        data = json.load(f)

        countries = []

        # length of list countries in json data for flexible number of countries
        for i in range(len(data["countries"])):

            countries.append(data["countries"][i]["country"])

        return countries


numberOfCountries = len(get_countries_list_from_json())


def show_frame1():

    clear_widgets()
    frame_1()


def show_frame3():

    clear_widgets()
    frame_3()


def start_game():

    clear_widgets()
    frame_2()


def create_buttons(answer, l_margin = 85, r_margin = 85):

    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    # button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#353535';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "color: #353535;" +
        "font-family: 'Helvetica';" +
        "font-size: 20px;" +
        "border-radius: 25px;" +
        "padding: 15px 0;" +
        "margin-top: 20px}" +
        "*:hover{background-color: '#C6FF33'}"
    )
    return button


def frame_1():

    # display logo
    image = QPixmap("logo_512px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50px;")
    widgets["logo"].append(logo)

    # button widget
    button = QPushButton("START")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#353535';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: '#353535';" +
        "padding: 25px 0;" +
        "margin: 100px 100px;}" +
        "*:hover{background: '#C6FF33';}"
    )
    button.clicked.connect(start_game)

    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)


def frame_2():

    question = QLabel("Where is your papaya from?")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: 'Helvetica';" +
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 75px;"
        "margin: 50px;")
    widgets["question"].append(question)

    fill_button_with_data()

    # buttons for countries start from second row in grid
    for i, j in zip(range(0, numberOfCountries), range(2, numberOfCountries + 2)):

        grid.addWidget(widgets["answers"][i], j, 0, 1, 2)

    image = QPixmap("logo_bottom_128px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50x; margin-bottom: 15px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    # number of rows is dependent on number of countries for flexible position on grid
    grid.addWidget(widgets["logo"][-1], numberOfCountries + 2, 0, 1, 2)


clickedAnswerButtonCountry = None


def which_button_was_clicked(clickedbutton):

    # sender() method of class QWidget saves whichever object sent a signal, here: clicked button
    global clickedAnswerButtonCountry
    clickedAnswerButtonCountry = clickedbutton.sender().text()
    # print(clickedAnswerButtonCountry)
    return clickedAnswerButtonCountry


def fill_button_with_data():

    for i in range(0, numberOfCountries):

        button = create_buttons(get_countries_list_from_json()[i])
        widgets["answers"].append(button)

        # every new button object stores the function below
        # if the button gets clicked, the lambda function gets executed
        # connect usually only requires the name of a  normal function, not a lambda function
        # but without the lambda it wasn't possible to pass the button argument
        button.clicked.connect(lambda: which_button_was_clicked(button))

        button.clicked.connect(show_frame3)


def frame_3():

    image = QPixmap("logo_bottom_128px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50x; margin-bottom: 15px;")
    widgets["logo"].append(logo)
    grid.addWidget(widgets["logo"][-1], numberOfCountries + 2, 0, 1, 2)

    print(clickedAnswerButtonCountry)


def get_main_season_list_from_json():

    with open("seasons.json", "r") as f:
        data = json.load(f)

        mainSeasons = []
        # length of list countries in json data for flexible number of countries
        for i in range(len(data["countries"])):
            mainSeasons.append(data["countries"][i]["mainSeason"])

        print(mainSeasons)

        return mainSeasons


def season_checker():

    currentmonth = date.today().month

    seasonlist = get_main_season_list_from_json()[0]

    if currentmonth in seasonlist:

        print("yes")

    else:

        print("no")


frame_1()


season_checker()


window.setLayout(grid)


window.show()


sys.exit(app.exec())
