# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
import yaml
import time
from collector.demoCollector import *

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        # ==== ==== ==== ====
        # GUI SETUP
        # ==== ==== ==== ====
        dialog.setObjectName("dialog")
        dialog.resize(450, 350)
        dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/DemoCollector.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        # ==== ==== ==== ====
        # DEFAULT
        # ==== ==== ==== ====
        self.settingsButton.clicked.connect(self.editSettings)
        self.collectButton.clicked.connect(self.getDemos)
        self.settings = []
        self.games = []

    # ==== ==== ==== ====
    # TRANSLATE GUI
    # ==== ==== ==== ====
    def retranslateUi(self, Dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.demoCountGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Demo count", None, QtGui.QApplication.UnicodeUTF8))
        self.mainGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.collectButton.setText(QtGui.QApplication.translate("dialog", "Collect them", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.progressGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.currentGameLabel.setText(QtGui.QApplication.translate("dialog", "...", None, QtGui.QApplication.UnicodeUTF8))


    def write(self, text):
        self.outputListWidget.addItem(text)
        self.outputListWidget.scrollToBottom()

    # ==== ==== ==== ====
    # GET DEMOS
    # ==== ==== ==== ====
    def getDemos(self):
        # ==== ==== ==== ====
        # ReLoad SETTINGS
        # ==== ==== ==== ====
        try:
            self.settings = yaml.load(open("files/settings.yml"))
            self.write("Settings loadet successfully")
        except:
            self.write("Settings load ERROR. YAML setting file is corrupt!")
            return False

        # LOAD GAMES
        self.games = [Game(**setting) for setting in self.settings['games']]

        # ==== ==== ==== ====
        # For all games load demos
        # ==== ==== ==== ====
        gamesNum = 0.0
        allDemosNum = 0

        for game in self.games:
            # Load game
            gamesNum += 1
            self.write("Loading game: %s" % game.name)

            # Game progress bar
            self.gamesProgressBar.setProperty("value", gamesNum / len(self.games) * 100)
            self.currentGameLabel.setText(QtGui.QApplication.translate("Dialog", game.name, None, QtGui.QApplication.UnicodeUTF8))

            # Test if game is valid... if all setting are correct
            if not game.test():
                self.write(" ... game is invalid!!!")
                #self.outputListWidget.scrollToBottom()
            else:
                self.write(" ... game is valid")


                # ==== ==== ==== ====
                # Get Demos for Game
                # ==== ==== ==== ====
                demoNum = 0.0

                for demo in game.copy():
                    self.write("     copy demo: %s" % demo.name)
                    demoNum += 1
                    allDemosNum += 1
                    # Game progress bar
                    self.lcdDemoNumber.display(allDemosNum)

    # ==== ==== ==== ====
    # EDIT SETTINGS
    # ==== ==== ==== ====
    def editSettings(self):
        try:
            os.popen("notepad %s/files/settings.yml" % os.getcwd())
        except:
            os.popen("vi %s/files/settings.yml" % os.getcwd())

# ==== ==== ==== ====
# MAIN
# ==== ==== ==== ====
if __name__ == '__main__':
    import sys
    print sys.argv
    print os.getcwd()
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.setupUi(dialog)
    sys.exit(dialog.exec_())
