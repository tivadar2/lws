from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from tinydb import TinyDB, where
import sys

class LwsMain(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        #bindings
        self.pushButton.clicked.connect(self.printsome)
        self.pushButton_addLang.clicked.connect(self.addLanguage)

    def printsome(self):
        db.insert({'van': 1})
        print(self.textEdit.toPlainText())

    def addLanguage(self):
        db.insert({'language': self.textEdit_language.toPlainText()})
        print('Language has been added.')
    
db = TinyDB('data/languages.json')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
