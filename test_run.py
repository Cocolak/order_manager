from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
import sys
#import pywinstyles


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    #pywinstyles.change_header_color(window, color="blue")
    window.show()
    app.exec_()
    