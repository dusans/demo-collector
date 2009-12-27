# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Dec 27 18:35:57 2009
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(450, 350)
        dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("DemoCollector.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.demoCountGroupBox = QtGui.QGroupBox(dialog)
        self.demoCountGroupBox.setGeometry(QtCore.QRect(10, 0, 120, 61))
        self.demoCountGroupBox.setObjectName("demoCountGroupBox")
        self.lcdDemoNumber = QtGui.QLCDNumber(self.demoCountGroupBox)
        self.lcdDemoNumber.setGeometry(QtCore.QRect(10, 22, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.lcdDemoNumber.setFont(font)
        self.lcdDemoNumber.setObjectName("lcdDemoNumber")
        self.mainGroupBox = QtGui.QGroupBox(dialog)
        self.mainGroupBox.setGeometry(QtCore.QRect(10, 60, 431, 281))
        self.mainGroupBox.setObjectName("mainGroupBox")
        self.outputListWidget = QtGui.QListWidget(self.mainGroupBox)
        self.outputListWidget.setGeometry(QtCore.QRect(10, 40, 411, 231))
        self.outputListWidget.setTabKeyNavigation(False)
        self.outputListWidget.setAlternatingRowColors(True)
        self.outputListWidget.setObjectName("outputListWidget")
        self.collectButton = QtGui.QPushButton(self.mainGroupBox)
        self.collectButton.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.collectButton.setFont(font)
        self.collectButton.setObjectName("collectButton")
        self.settingsButton = QtGui.QPushButton(self.mainGroupBox)
        self.settingsButton.setGeometry(QtCore.QRect(350, 20, 75, 21))
        self.settingsButton.setObjectName("settingsButton")
        self.progressGroupBox = QtGui.QGroupBox(dialog)
        self.progressGroupBox.setGeometry(QtCore.QRect(140, 0, 301, 61))
        self.progressGroupBox.setObjectName("progressGroupBox")
        self.gamesProgressBar = QtGui.QProgressBar(self.progressGroupBox)
        self.gamesProgressBar.setGeometry(QtCore.QRect(10, 40, 291, 16))
        self.gamesProgressBar.setProperty("value", 24)
        self.gamesProgressBar.setObjectName("gamesProgressBar")
        self.currentGameLabel = QtGui.QLabel(self.progressGroupBox)
        self.currentGameLabel.setGeometry(QtCore.QRect(10, 20, 271, 20))
        self.currentGameLabel.setObjectName("currentGameLabel")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.demoCountGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Demo count", None, QtGui.QApplication.UnicodeUTF8))
        self.mainGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.collectButton.setText(QtGui.QApplication.translate("dialog", "Collect them", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.progressGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.currentGameLabel.setText(QtGui.QApplication.translate("dialog", "...", None, QtGui.QApplication.UnicodeUTF8))

import recorceFile_rc
