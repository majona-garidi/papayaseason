import calendar
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QFontDatabase
import json
from datetime import date


widgets = {

    "logo": [],
    "button": [],
    "question": [],
    "answers": [],
    "result": [],
    "animation": []

}

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Papaya Season")
# several buttons are created (downwards the GUI) based on how many countries
# there are in the json data
# therefore adjustSize() is used to react to the varying quantity of buttons
window.adjustSize()
window.setFixedWidth(700)
window.setStyleSheet("background: 'white'")

grid = QGridLayout()


clicked_answer_button_country = None


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


number_of_countries = len(get_countries_list_from_json())


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
        "*{border: 2px solid '#353535';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" + 
        "color: #353535;" +
        "font-size: 20px;" +
        "border-radius: 25px;" +
        "padding: 15px 0;" +
        "margin-top: 20px}" +
        "*:hover{background-color: '#C6FF33'}"
    )

    return button


def frame_1():

    # display logo
    image = QPixmap("icons/logo_500px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50px;")
    widgets["logo"].append(logo)

    # button widget
    button = QPushButton("START")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
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
    #question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: 'Helvetica';" +
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 75px;"
        "margin: 50px;")

    widgets["question"].append(question)

    fill_button_with_data()

    # buttons for countries start from second row in grid
    for i, j in zip(range(0, number_of_countries), range(2, number_of_countries + 2)):

        grid.addWidget(widgets["answers"][i], j, 0, 1, 2)

    image = QPixmap("icons/1.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50x; margin-bottom: 15px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    # number of rows is dependent on number of countries for flexible position on grid
    grid.addWidget(widgets["logo"][-1], number_of_countries + 2, 0, 1, 2)


def which_button_was_clicked(clicked_button):

    # sender() method of class QWidget saves whichever object sent a signal, here: clicked button
    global clicked_answer_button_country
    clicked_answer_button_country = clicked_button.sender().text()
    return clicked_answer_button_country


def fill_button_with_data():

    for i in range(0, number_of_countries):

        button = create_buttons(get_countries_list_from_json()[i])
        widgets["answers"].append(button)

        # every new button object stores the function below
        # if the button gets clicked, the lambda function gets executed
        # connect usually only requires the name of a  normal function, not a lambda function
        # but without the lambda it wasn't possible to pass the button argument
        button.clicked.connect(lambda: which_button_was_clicked(button))

        button.clicked.connect(show_frame3)


def frame_3():

    result = QLabel(answer_sentence())
    result.setAlignment(QtCore.Qt.AlignCenter)
    result.setWordWrap(True)
    result.setStyleSheet(
        "font-family: 'Helvetica';" +
        "font-size: 25px;" +
        "color: '#353535';"
        "padding: 75px;"
        "margin: 50px;"
    )
    widgets["result"].append(result)
    grid.addWidget(widgets["result"][-1], 4, 0, 1, 2)

    image = QPixmap("icons/logo_110x110.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50x; margin-bottom: 15px;")
    widgets["logo"].append(logo)
    grid.addWidget(widgets["logo"][-1], number_of_countries + 2, 0, 1, 2)


main_season_for_clicked_button = None


def get_main_season_list_from_clicked_button():

    with open("seasons.json", "r") as f:
        data = json.load(f)

    for country_dict in data["countries"]:
        if country_dict["country"] == clicked_answer_button_country:
            newlist = country_dict["mainSeason"]
            return newlist


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
        if country_dict["country"] == clicked_answer_button_country:

            return country_dict["availability"]


def season_check():

    global current_month
    current_month = date.today().month

    season_list = get_main_season_list_from_clicked_button()

    if current_month in season_list:

        return True

    else:

        return False


def answer_sentence():

    if season_check() == True:

        place_affirming_animation_on_grid()

        return "It's papaya season in " + clicked_answer_button_country + ". " + "The season ends in " + end_of_papaya_season()

    else:

        place_warning_animation_on_grid()

        return "The next papaya season in " + clicked_answer_button_country + " starts in " + next_papaya_season()


def place_warning_animation_on_grid():

    label = QLabel()
    animation = QMovie("icons/warning_500px.gif")
    label.setMovie(animation)
    animation.start()
    widgets["animation"].append(animation)
    label.setAlignment(QtCore.Qt.AlignCenter)
    grid.addWidget(label, 1, 0, 3, 2)


def place_affirming_animation_on_grid():

        label = QLabel()
        animation = QMovie("icons/confirmation_500px.gif")
        label.setMovie(animation)
        animation.start()
        widgets["animation"].append(animation)
        label.setAlignment(QtCore.Qt.AlignCenter)
        grid.addWidget(label, 1, 0, 3, 2)


frame_1()


window.setLayout(grid)


window.show()


sys.exit(app.exec())
