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
        print(self.textEdit.toPlainText())

    def addLanguage(self):
        typedLanguage = self.lineEdit_language.toPlainText()
        res = languages.search(where('language') == typedLanguage)
        if not res: # typedLanguage isn't in the database yet
            languages.insert({'language': typedLanguage})
            print('Language has been added.')
        else:
            print('Language is already in the database.')  
    
languages = TinyDB('data/languages.json')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
