import calendar
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QFont, QFontDatabase
import json
from datetime import date
import os

# we need absolute path so the font file can be found in users directory
# font file needs to be in same directory as main.py
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

widgets = {

    "logo": [],
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

window = QWidget()
window.setWindowTitle("Papaya Season")
window.adjustSize()
window.setMinimumSize(600, 840)
window.setStyleSheet(
    "background: '#F2CEE8'"
)

grid = QGridLayout()

def load_font(font_file_name):
    path_to_font_file = os.path.join(ROOT_DIR, font_file_name)
    id = QFontDatabase.addApplicationFont(path_to_font_file)
    if id < 0:
        print(f"Font file {path_to_font_file} not found")
    font_families = QFontDatabase.applicationFontFamilies(id)
    font_name = font_families[0]
    return QFont(font_name)


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


def show_frame2():

    clear_widgets()
    frame_2()


def show_frame3():

    clear_widgets()
    frame_3()


def start_game():

    clear_widgets()
    frame_2()


def create_buttons(answer, l_margin = 100, r_margin = 100):

    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font("DidactGothic-Regular.ttf")
    button.setFont(button_font)
    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" + 
        "color: #353535;" +
        "font-size: 20px;" +
        "padding: 12px 0;" +
        "margin-top: 10px}" +
        "*:hover{background-color: '#C6FF33'}"
    )

    return button


def frame_1():

    image = QPixmap("icons/logo_300px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 20px;"
    )
    widgets["logo"].append(logo)


    header = QLabel("Enjoy better papayas - go by their harvest time")
    font_header = load_font("DidactGothic-Regular.ttf")
    header.setFont(font_header)
    widgets["header"].append(header)
    header.setAlignment(QtCore.Qt.AlignCenter)
    header.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding-top: 40px;" +
        "padding-bottom: 10px;"
        )


    description = QLabel(
        "Simply choose where your papaya is from and let" + "\n" +
        "the app check the harvest time of the country" + "\n" +
        "that you've chosen. Enjoy a fresher fruit."
    )

    widgets["description"].append(description)
    description.setAlignment(QtCore.Qt.AlignCenter)
    font_description = load_font("DidactGothic-Regular.ttf")
    description.setFont(font_description)
    description.setStyleSheet(
        "font-size: 20px;" +
        "color: '#353535';"
    )


    button = QPushButton("Start")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font("DidactGothic-Regular.ttf")
    button.setFont(button_font)
    button.setStyleSheet(
        "*{border: 2px solid '#353535';" +
        "font-size: 30px;" +
        "color: '#353535';" +
        "padding: 2px 0;" +
        "margin: 85px 160px;}" +
        "*:hover{background: '#C6FF33';}"
    )

    button.clicked.connect(start_game)

    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["header"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["description"][-1], 5, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 6, 0, 1, 2)


def frame_2():

    question = QLabel("Where is your papaya from?")
    question.setAlignment(QtCore.Qt.AlignCenter)
    #question.setWordWrap(True)
    question_font = load_font("DidactGothic-Regular.ttf")
    question.setFont(question_font)
    question.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 60px;"+
        "margin-top: 20px;"
    )

    widgets["question"].append(question)

    fill_button_with_data()

    # buttons for countries start from second row in grid
    for i, j in zip(range(0, number_of_countries), range(2, number_of_countries + 2)):

        grid.addWidget(widgets["answers"][i], j, 0, 1, 2)

    image = QPixmap("icons/logo_110px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 50x;" +
        "margin-bottom: 15px;"
    )
    widgets["logo"].append(logo)

    grid.addWidget(widgets["question"][-1], 0, 0, 1, 2)
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


def place_animation_on_grid():

    if season_check() == True:

        place_affirming_animation_on_grid()

    else:

        place_warning_animation_on_grid()


def frame_3():

    place_animation_on_grid()

    result = QLabel(answer_sentence())
    result.setAlignment(QtCore.Qt.AlignCenter)
    result.setWordWrap(True)
    result_font = load_font("DidactGothic-Regular.ttf")
    result.setFont(result_font)
    result.setStyleSheet(
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 50px;"
    )
    widgets["result"].append(result)
    grid.addWidget(widgets["result"][-1], 4, 0, 2, 2)

    button = QPushButton("Try another country")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_font = load_font("DidactGothic-Regular.ttf")
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

    grid.addWidget(widgets["back"][-1], 5, 0, 2, 2)


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

        return "It's papaya season in " + clicked_answer_button_country + ". " + "The season ends in " + end_of_papaya_season() + "."

    else:

        return "The next papaya season in " + clicked_answer_button_country + " starts in " + next_papaya_season() + "."


def place_warning_animation_on_grid():

    label = QLabel()
    animation = QMovie("icons/warning_500px.gif")
    label.setMovie(animation)
    animation.start()
    widgets["animation"].append(label)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(
        "margin-top: 20px;"
    )
    grid.addWidget(widgets["animation"][-1], 0, 0, 3, 2)


def place_affirming_animation_on_grid():

        label = QLabel()
        animation = QMovie("icons/confirmation_500px.gif")
        label.setMovie(animation)
        animation.start()
        widgets["animation"].append(label)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet(
            "margin-top: 20px;"
        )
        grid.addWidget(widgets["animation"][-1], 0, 0, 3, 2)


frame_1()


window.setLayout(grid)


window.show()


sys.exit(app.exec())
