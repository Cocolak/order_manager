from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec_()
    