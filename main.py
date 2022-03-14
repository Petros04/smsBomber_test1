#progam
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import pyautogui as pg
import random
import time
from form import *


def spam():
        url = 'https://www.instagram.com/direct/inbox/'
        webbrowser.open_new_tab(url)

        pg.moveTo(300, 300)

        time.sleep(3)
        pg.click()

        text = ('LAAAAA','BLAAA')
        time.sleep(5)
        for i in range(100):
                a = random.choice(text)
                pg.write(a)
                pg.press('enter')
                time.sleep(0.2)


    #    self.lineEdit_2.setEnabled(False)
#if self.lineEdit.setText() == "":
 #       self.lineEdit_2.setEnabled(False)