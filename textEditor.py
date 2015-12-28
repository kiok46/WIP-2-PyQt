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
        self.updateStatusBar()

    def updateMenuBar(self):
        self.fileMenu = self.menuBar.addMenu('&File')
        self.editMenu = self.menuBar.addMenu('&Edit')
        self.viewMenu = self.menuBar.addMenu('&View')
        self.insertMenu = self.menuBar.addMenu('&Insert')

    def updateFormatBar(self):
        print "updateFormatBar"
        # #Code

    def updateStatusBar(self):
        self.zoomSlider = QSlider(Qt.Horizontal, self.statusBar)
        self.zoomSlider.setTickPosition(QSlider.TicksAbove)
        self.zoomSlider.setTickInterval(50)
        self.zoomSlider.setValue(50)
        self.curZoomValue = 50
        self.statusBar.addWidget(self.zoomSlider)
        self.connect(self.zoomSlider, SIGNAL("valueChanged(int)"), self.zoom)

    def zoom(self):
        value = self.zoomSlider.value()
        if self.curZoomValue > value:
            self.textArea.zoomOut((self.curZoomValue - value))
        else:
            self.textArea.zoomIn((value - self.curZoomValue))
        self.curZoomValue = value

def main():
    app = QApplication(sys.argv)
    textEditor = mainWindow()
    textEditor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
