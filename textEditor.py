#!/usr/bin/python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.updateUI()

    def updateUI(self):
        self.textArea = QTextEdit()
        self.setCentralWidget(self.textArea)


def main():
    app = QApplication(sys.argv)
    textEditor = mainWindow()
    textEditor.show()
    sys.exit(app.exec_())

main()
