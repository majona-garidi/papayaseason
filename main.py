import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import json


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
        #length of list countries in json data for flexible number of countries
        for i in range(len(data["countries"])):
            countries.append(data["countries"][i]["country"])

        return countries


numberOfCountries = len(get_countries_list_from_json())

def show_frame1():
    clear_widgets()
    frame_1()


def start_game():
    clear_widgets()
    frame_2()


def create_buttons(answer, l_margin = 85, r_margin = 85):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    #button.setFixedWidth(485)
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
    button.clicked.connect(show_frame1)
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

    for i in range(0, numberOfCountries):
        button = create_buttons(get_countries_list_from_json()[i])
        widgets["answers"].append(button)

    #buttons for countries start from second row in grid
    for i, j in zip(range(0, numberOfCountries),range(2, numberOfCountries + 2)):
        grid.addWidget(widgets["answers"][i], j, 0, 1, 3)

    image = QPixmap("logo_bottom_128px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50x; margin-bottom: 15px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["question"][-1], 1, 0, 1, 3)
    # number of rows is dependent on number of countries for flexible position on grid
    grid.addWidget(widgets["logo"][-1], numberOfCountries + 2, 0, 1, 3)


frame_1()


window.setLayout(grid)


window.show()


sys.exit(app.exec())