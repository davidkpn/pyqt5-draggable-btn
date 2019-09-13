from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow
import sys

from draggable import Draggable

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Draggable")
        self.object = Draggable("object", self)
        self.object.setGeometry(200, 200, 300, 400)
        self.object.setMinimumSize(60,20)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    app.exec_()

sys.exit(main())
