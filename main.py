from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
import sys

class LwsGui(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
