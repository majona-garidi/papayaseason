import sys
import json
import calendar
import os

import model
import view

from pathlib import Path

from typing import Union

from datetime import date

from PyQt5 import QtCore

from PyQt5.QtGui import QPixmap, QMovie, QCursor, QFont, QFontDatabase

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout