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
        self.menuBar = self.menuBar()
        self.updateMenuBar()
        self.formatBar = self.addToolBar("Format")
        self.formatBar.setMovable(False)
        self.formatBar.setFloatable(False)
        self.updateFormatBar()
        self.statusBar = self.statusBar()

    def updateMenuBar(self):
        self.fileMenu = self.menuBar.addMenu('&File')
        self.editMenu = self.menuBar.addMenu('&Edit')
        self.viewMenu = self.menuBar.addMenu('&View')
        self.insertMenu = self.menuBar.addMenu('&Insert')

    def updateFormatBar(self):
        print "updateFormatBar"
        # #Code


def main():
    app = QApplication(sys.argv)
    textEditor = mainWindow()
    textEditor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
