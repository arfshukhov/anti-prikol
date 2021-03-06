import time

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from win32api import GetSystemMetrics

import sys

from PIL import ImageGrab

import random

import keyboard

import threading
import asyncio
import os


SYS_W = GetSystemMetrics(0)
SYS_H = GetSystemMetrics(1)

image = ImageGrab.grab(bbox=(0, 0, SYS_W,SYS_H))
image.save('sc.png')


class Main(QWidget):
    def __init__(self):
        super().__init__()

    def init_ui(self):
        self.setFixedSize(SYS_W, SYS_H)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        QShortcut(QKeySequence("Shift+Alt+Q"), self, quit)
        #keyboard.add_hotkey("alt + f4", lambda: None, suppress=True)


        self.show()
        self.lab = QLabel(self)
        self.lab.setGeometry(0, 0, SYS_W, SYS_H)
        self.lab.setText("")
        self.lab.setStyleSheet("background-image : url(sc.png); color : white")
        self.lab.setFont(QFont("Bold", 130))
        self.lab.show()

    def this_method_should_freeze_ur_pc(self):
        for i in range(20):
            self.draw_pricall()


    def draw_pricall(self):
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0 , 0)")
        self.label.setText("LOL LOL LOL LOL LOL")
        self.label.setGeometry(random.randrange(0, SYS_W), random.randrange(0, SYS_H), 200, 100)
        self.label.setFont(QFont("Bold", 14))
        self.label.show()
        asyncio.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()

    threading.Thread(target=main.init_ui()).start()
    threading.Thread(target=main.this_method_should_freeze_ur_pc()).start()

    os.remove("sc.png")
    app.exec()