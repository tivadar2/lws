from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
import sys

class LwsGui(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.pushButton.clicked.connect(self.printsome)

    def printsome(self):
        print(self.textEdit.toPlainText())
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsGui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
