#!/usr/bin/env python

"""PyQt4 port of the layouts/basiclayout example from Qt v4.x"""

from PyQt4 import QtCore, QtGui


class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()


        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 526)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(400, 220, 61, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 130, 581, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtGui.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 170, 581, 16))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 220, 381, 291))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 110, 46, 14))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 150, 46, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 46, 14))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(400, 200, 71, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Collect them", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Game Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Game:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Demo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Demo count:", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
