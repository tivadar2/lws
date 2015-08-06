from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from tinydb import TinyDB, where
import sys
import urllib.parse, urllib.request
from bs4 import BeautifulSoup

class LwsMain(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        # load languages to choose from
        for language in languagesDb.all():
            self.comboBox_languages.addItem(language.get('language'))

        # bindings
        self.pushButton.clicked.connect(self.printsome)
        self.pushButton_addLang.clicked.connect(self.addLanguage)
        self.textEdit.selectionChanged.connect(self.selChanged)

    def printsome(self):
        parameters = {}
        parameters['from'] = 'rus'
        parameters['to'] = 'eng'
        
        allParameter = urllib.parse.urlencode({'from': 'rus', 'to': 'eng'})
        url = 'http://tatoeba.org/eng/sentences/search?'
        url = url + allParameter
        response = urllib.request.urlopen(url)
        html = response.read()

        parsedHtml = BeautifulSoup(html, 'html.parser')
        print(parsedHtml.find('div', attrs={'class': 'sentences_set'}).findAll('div', attrs={'lang': 'en'})[1].contents)

    def addLanguage(self):
        typedLanguage = self.lineEdit_language.toPlainText()
        res = languages.search(where('language') == typedLanguage)
        if not res: # typedLanguage isn't in the database yet
            languages.insert({'language': typedLanguage})
            print('Language has been added.')
        else:
            print('Language is already in the database.')

    def selChanged(self):
        cursor = self.textEdit.textCursor()
        beginPos = cursor.selectionStart()
        endPos = cursor.selectionEnd()
        if beginPos != endPos:
            wholeText = self.textEdit.toPlainText()
            selectedText = wholeText[beginPos:endPos]
            print(selectedText)
    
languagesDb = TinyDB('data/languages.json')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
