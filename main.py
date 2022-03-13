#progam
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import pyautogui as pg
import random
import time


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


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(297, 312)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                Dialog.setFont(font)
                Dialog.setStyleSheet("")
                self.lineEdit = QtWidgets.QLineEdit(Dialog)
                self.lineEdit.setGeometry(QtCore.QRect(30, 40, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit.setFont(font)
                self.lineEdit.setText("")
                self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_2.setGeometry(QtCore.QRect(30, 70, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setText("")
                self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_3.setGeometry(QtCore.QRect(30, 100, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setText("")
                self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_4.setGeometry(QtCore.QRect(30, 130, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit_4.setFont(font)
                self.lineEdit_4.setText("")
                self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_5.setGeometry(QtCore.QRect(30, 160, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit_5.setFont(font)
                self.lineEdit_5.setText("")
                self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_6.setGeometry(QtCore.QRect(30, 190, 231, 20))
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(50)
                self.lineEdit_6.setFont(font)
                self.lineEdit_6.setText("")
                self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.checkBox = QtWidgets.QCheckBox(Dialog)
                self.checkBox.setGeometry(QtCore.QRect(270, 40, 70, 17))
                self.checkBox.setText("")
                self.checkBox.setObjectName("checkBox")
                self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
                self.checkBox_2.setGeometry(QtCore.QRect(270, 70, 70, 17))
                self.checkBox_2.setText("")
                self.checkBox_2.setObjectName("checkBox_2")
                self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
                self.checkBox_3.setGeometry(QtCore.QRect(270, 100, 70, 17))
                self.checkBox_3.setText("")
                self.checkBox_3.setObjectName("checkBox_3")
                self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
                self.checkBox_4.setGeometry(QtCore.QRect(270, 130, 70, 17))
                self.checkBox_4.setText("")
                self.checkBox_4.setObjectName("checkBox_4")
                self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
                self.checkBox_5.setGeometry(QtCore.QRect(270, 160, 70, 17))
                self.checkBox_5.setText("")
                self.checkBox_5.setObjectName("checkBox_5")
                self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
                self.checkBox_6.setGeometry(QtCore.QRect(270, 190, 70, 17))
                self.checkBox_6.setText("")
                self.checkBox_6.setObjectName("checkBox_6")
                self.timeEdit = QtWidgets.QTimeEdit(Dialog)
                self.timeEdit.setGeometry(QtCore.QRect(30, 230, 118, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.timeEdit.setFont(font)
                self.timeEdit.setMaximumTime(QtCore.QTime(1, 59, 0))
                self.timeEdit.setObjectName("timeEdit")
                self.spinBox = QtWidgets.QSpinBox(Dialog)
                self.spinBox.setGeometry(QtCore.QRect(190, 230, 91, 22))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.spinBox.setFont(font)
                self.spinBox.setMaximum(500)
                self.spinBox.setSingleStep(10)
                self.spinBox.setObjectName("spinBox")
                self.pushButton = QtWidgets.QPushButton(Dialog)
                self.pushButton.setGeometry(QtCore.QRect(80, 270, 151, 23))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton.setFont(font)
                self.pushButton.setObjectName("pushButton")

                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(26, 10, 241, 20))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setMouseTracking(False)
                self.label.setObjectName("label")

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)


        def retranslateUi(self, Dialog):  
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("SmsBomber", "SmsBomber"))
                self.pushButton.setText(_translate("Dialog", "Старт"))

                self.label.setText(_translate("Dialog", "Введите ваш текст для спама"))



if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())


