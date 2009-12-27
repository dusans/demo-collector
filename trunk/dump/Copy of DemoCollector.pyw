# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
import yaml
import time
from collector.collectDemos import *

class Ui_Dialog(QtGui.QDialog):

    def setupUi(self, Dialog):
        # MAIN
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("DemoCollector.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        # BUTTONS
        self.settingsButton = QtGui.QPushButton(Dialog)
        self.settingsButton.setGeometry(QtCore.QRect(540, 70, 75, 23))
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.clicked.connect(self.editSettings)
        self.collectButton = QtGui.QPushButton(Dialog)
        self.collectButton.setGeometry(QtCore.QRect(10, 70, 191, 31))
        self.collectButton.clicked.connect(self.getDemos)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.collectButton.setFont(font)
        self.collectButton.setObjectName("collectButton")
        # PROGRESS BAR
        self.gamesProgressBar = QtGui.QProgressBar(Dialog)
        self.gamesProgressBar.setGeometry(QtCore.QRect(10, 130, 581, 16))
        self.gamesProgressBar.setProperty("value", 0)
        self.gamesProgressBar.setObjectName("gamesProgressBar")
        self.demoProgressBar = QtGui.QProgressBar(Dialog)
        self.demoProgressBar.setGeometry(QtCore.QRect(10, 170, 581, 16))
        self.demoProgressBar.setProperty("value", 0)
        self.demoProgressBar.setObjectName("DemoProgressBar")
        # DEMO COUNTER
        self.lcdDemoNumber = QtGui.QLCDNumber(Dialog)
        self.lcdDemoNumber.setGeometry(QtCore.QRect(520, 220, 61, 23))
        self.lcdDemoNumber.setObjectName("lcdDemoNumber")
        self.lcdDemoNumber.display(0)
        # OUTPUT text
        self.outputListWidget = QtGui.QListWidget(Dialog)
        self.outputListWidget.setGeometry(QtCore.QRect(10, 220, 500, 291))
        self.outputListWidget.setObjectName("outputListWidget")
        # LABELS
        #  Title
        self.titleLabel = QtGui.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(140, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.gameLabel = QtGui.QLabel(Dialog)
        self.gameLabel.setGeometry(QtCore.QRect(20, 110, 31, 16))
        self.gameLabel.setObjectName("gameLabel")
        self.demoLabel = QtGui.QLabel(Dialog)
        self.demoLabel.setGeometry(QtCore.QRect(20, 150, 31, 16))
        self.demoLabel.setObjectName("demoLabel")
        self.currentGameLabel = QtGui.QLabel(Dialog)
        self.currentGameLabel.setGeometry(QtCore.QRect(60, 110, 250, 14))
        self.currentGameLabel.setObjectName("currentGameLabel")
        self.currentDemoLabel = QtGui.QLabel(Dialog)
        self.currentDemoLabel.setGeometry(QtCore.QRect(60, 150, 450, 14))
        self.currentDemoLabel.setObjectName("currentDemoLabel")
        self.outputLabel = QtGui.QLabel(Dialog)
        self.outputLabel.setGeometry(QtCore.QRect(20, 200, 46, 14))
        self.outputLabel.setObjectName("outputLabel")
        self.demoCountLabel = QtGui.QLabel(Dialog)
        self.demoCountLabel.setGeometry(QtCore.QRect(520, 200, 71, 16))
        self.demoCountLabel.setObjectName("demoCountLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.settings = []
        self.games = []

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.collectButton.setText(QtGui.QApplication.translate("Dialog", "Collect them", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("Dialog", "Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.gameLabel.setText(QtGui.QApplication.translate("Dialog", "Game:", None, QtGui.QApplication.UnicodeUTF8))
        self.demoLabel.setText(QtGui.QApplication.translate("Dialog", "Demo:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentGameLabel.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.currentDemoLabel.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.outputLabel.setText(QtGui.QApplication.translate("Dialog", "Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.demoCountLabel.setText(QtGui.QApplication.translate("Dialog", "Demo count:", None, QtGui.QApplication.UnicodeUTF8))

    def getDemos(self):
        #-------------------------------------------------------------------------------
        # ReLoad SETTINGS
        try:
            self.settings = yaml.load(open("settings/settings.yml"))
            self.outputListWidget.addItem("Settings loadet successfully")
        except:
            self.outputListWidget.addItem("Settings load ERROR. YAML setting file is corrupt!")
            return False

        self.games = [Game(**setting) for setting in self.settings['games']]

        #-------------------------------------------------------------------------------
        # For all games load demos
        gamesNum = 0.0
        allDemosNum = 0

        for game in self.games:
            # Load game
            gamesNum += 1
            self.outputListWidget.addItem("Loading game: %s" % game.name)

            # Game progress bar
            self.gamesProgressBar.setProperty("value", gamesNum / len(self.games) * 100)
            self.currentGameLabel.setText(QtGui.QApplication.translate("Dialog", game.name, None, QtGui.QApplication.UnicodeUTF8))

            # Test if game is valid... if all setting are correct
            if not game.test():
                self.outputListWidget.addItem(" ... game is invalid!!!")
            else:
                self.outputListWidget.addItem(" ... game is valid")

                #-------------------------------------------------------------------------------
                # Get Demos for Game
                #-------------------------------------------------------------------------------
                demoNum = 0.0

                for demo in game.copy():
                    self.outputListWidget.addItem("     copy demo: %s" % demo.name)
                    demoNum += 1
                    allDemosNum += 1
                    # Game progress bar
                    self.demoProgressBar.setProperty("value", demoNum / len(game.demos) * 100)
                    self.currentDemoLabel.setText(QtGui.QApplication.translate("Dialog", demo.name, None, QtGui.QApplication.UnicodeUTF8))
                    self.lcdDemoNumber.display(allDemosNum)

                # Default set to 100% testing
                self.demoProgressBar.setProperty("value", 100)

    def editSettings(self):
        try:
            os.popen("notepad %s/settings/settings.yml" % os.getcwd())
        except:
            os.popen("vi %s/settings/settings.yml" % os.getcwd())

if __name__ == '__main__':

    import sys
    print sys.argv
    print os.getcwd()
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.setupUi(dialog)
    sys.exit(dialog.exec_())
