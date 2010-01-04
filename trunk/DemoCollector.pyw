# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
from subprocess import Popen
from collector.demoCollector import *

class Ui_Dialog(QtGui.QDialog):

    def setupUi(self, Dialog):
        # ==== ==== ==== ====
        # GUI SETUP
        # ==== ==== ==== ====
        dialog.setObjectName("dialog")
        dialog.resize(519, 350)
        dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/icons/DemoCollector.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.mainGroupBox = QtGui.QGroupBox(dialog)
        self.mainGroupBox.setGeometry(QtCore.QRect(10, 0, 501, 341))
        self.mainGroupBox.setObjectName("mainGroupBox")
        self.outputListWidget = QtGui.QListWidget(self.mainGroupBox)
        self.outputListWidget.setGeometry(QtCore.QRect(10, 40, 481, 291))
        self.outputListWidget.setTabKeyNavigation(False)
        self.outputListWidget.setAlternatingRowColors(True)
        self.outputListWidget.setObjectName("outputListWidget")
        self.collectButton = QtGui.QPushButton(self.mainGroupBox)
        self.collectButton.setGeometry(QtCore.QRect(10, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.collectButton.setFont(font)
        self.collectButton.setObjectName("collectButton")
        self.settingsButton = QtGui.QPushButton(self.mainGroupBox)
        self.settingsButton.setGeometry(QtCore.QRect(380, 20, 111, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.lcdDemoNumber = QtGui.QLCDNumber(self.mainGroupBox)
        self.lcdDemoNumber.setGeometry(QtCore.QRect(230, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.lcdDemoNumber.setFont(font)
        self.lcdDemoNumber.setObjectName("lcdDemoNumber")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        # ==== ==== ==== ====
        # MY DEFAULT
        # ==== ==== ==== ====
        self.settingsFilePath = "files/settings.yml"
		# bind buttons actions
        self.settingsButton.clicked.connect(self.editSettings)
        self.collectButton.clicked.connect(self.collect)


        # ==== ICONS ====
        self.icons = {  "OK": "files/icons/NormalIcon.ico","Error": "files/icons/ModifiedIcon.ico",
                        "Warning": "files/icons/ConflictIcon.ico", "Add": "files/icons/AddedIcon.ico",
                        "Ignore": "files/icons/IgnoredIcon.ico", "Delete": "files/icons/DeletedIcon.ico"}

    # ==== ==== ==== ====
    # TRANSLATE GUI
    # ==== ==== ==== ====
    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Demo Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.mainGroupBox.setTitle(QtGui.QApplication.translate("dialog", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.collectButton.setText(QtGui.QApplication.translate("dialog", "Collect them", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))

    # ==== ==== ==== ====
    # Write to CONSOLE
    # using self.icons
    # ==== ==== ==== ====
    def write(self, message):
        if isinstance(message, Message):
            item = QtGui.QListWidgetItem(message.text)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.icons[message.messageType]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.outputListWidget.addItem(item)
        else:
            self.outputListWidget.addItem(message)

        self.outputListWidget.scrollToBottom()

    # ==== ==== ==== ====
    # COLLECT
    # ==== ==== ==== ====
    def collect(self):
        collector = Collector(self.settingsFilePath, self.write, self.lcdDemoNumber.display)
        collector.collect()

    # ==== ==== ==== ====
    # EDIT SETTINGS
    # ==== ==== ==== ====
    def editSettings(self):
        if not os.path.exists("%s/%s" % (os.getcwd(), self.settingsFilePath)):
            open(self.settingsFilePath, "w").write(open("%s.%s" % (self.settingsFilePath, "example")).read())

        try:
            Popen(["notepad", "%s/%s" % (os.getcwd(), self.settingsFilePath)])
        except:
            Popen(["vi", "%s/%s" % (os.getcwd(), self.settingsFilePath)])

# ==== ==== ==== ====
# MAIN
# ==== ==== ==== ====
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.setupUi(dialog)
    sys.exit(dialog.exec_())
