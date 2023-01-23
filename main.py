import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


widgets = {
    "logo": [],
    "button": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Papaya Season")
window.setFixedWidth(1000)
#window.move(2700, 200)
window.setStyleSheet("background: 'white'")

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_frame1():
    clear_widgets()
    frame1()


def start_game():
    clear_widgets()
    frame2()

def create_buttons(answer, l_margin, r_margin):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#353535';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "color: #353535;" +
        "font-family: 'Helvetica';" +
        "font-size: 16px;" +
        "border-radius: 25px;" +
        "padding: 15px 0;" +
        "margin-top: 20px}" +
        "*:hover{background: '#C6FF33'}"
    )
    button.clicked.connect(show_frame1)
    return button

def frame1():
    #display logo
    image = QPixmap("logo_512px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    #button widget
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


def frame2():
    question = QLabel("Placeholder text will go here")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: 'Helvetica';" +
        "font-size: 25px;" +
        "color: '#353535';" +
        "padding: 75px;"
        "margin: 100px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons("answer1", 85, 5)
    button2 = create_buttons("answer2", 5, 85)
    button3 = create_buttons("answer3", 85, 5)
    button4 = create_buttons("answer4", 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    image = QPixmap("logo_bottom_128px.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 75x; margin-bottom: 30px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1, 2)


frame1()


window.setLayout(grid)

window.show()
sys.exit(app.exec())