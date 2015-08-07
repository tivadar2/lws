from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from menubar import MenuBar
from tinydb import TinyDB, where
import sys
import string
import urllib.parse, urllib.request
from bs4 import BeautifulSoup

class LwsMain(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        # load languages to choose from
        for language in languagesDb.all():
            self.comboBox_languages.addItem(language.get('language'))

        # initialize menu bar
        self.menuBar = MenuBar(self.stackedWidget_main)

        # bindings
        self.pushButton.clicked.connect(self.printsome)
        self.pushButton_addLang.clicked.connect(self.addLanguage)
        self.pushButton_addSentence.clicked.connect(self.addSentence)
        self.textEdit_sentence.selectionChanged.connect(self.selChanged)

        # menu bar bindings
        self.action_addSentence.triggered.connect(self.menuBar.changeToAddSentence)
        self.action_addLanguage.triggered.connect(self.menuBar.changeToAddLanguage)
        self.action_viewTerms.triggered.connect(self.menuBar.changeToViewTerms)
        self.action_viewSentences.triggered.connect(self.menuBar.changeToViewSentences)

        # setup tableWidget_terms
        headers = ['Term', 'Translation', 'Score']
        self.tableWidget_terms.setColumnCount(3)
        self.tableWidget_terms.setHorizontalHeaderLabels(headers)

        # setup tableWidget_sentences
        headers = ['Sentence', 'Translation', 'Total Words', 'Unknown words']
        self.tableWidget_sentences.setColumnCount(4)
        self.tableWidget_sentences.setHorizontalHeaderLabels(headers)
        for sentence in sentencesDb.all():
            self.tableWidget_sentences.insertRow(self.tableWidget_sentences.rowCount()) # place it at action stackwidget change
            self.tableWidget_sentences.setItem(self.tableWidget_sentences.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(sentence['sentence']))
            self.tableWidget_sentences.setItem(self.tableWidget_sentences.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(sentence['translation']))
            self.tableWidget_sentences.setItem(self.tableWidget_sentences.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(str(sentence['totalWords'])))
            self.tableWidget_sentences.setItem(self.tableWidget_sentences.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(sentence['TODOs'])))
        
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
        res = languagesDb.search(where('language') == typedLanguage)
        if not res: # typedLanguage isn't in the database yet
            languagesDb.insert({'language': typedLanguage})
            print('Language has been added.')
        else:
            print('Language is already in the database.')

    def addSentence(self):
        sentence = self.textEdit_sentence.toPlainText()
        withoutPunctuation = ''.join(c for c in sentence if c not in string.punctuation)
        print(withoutPunctuation)
        knownWords = 0
        totalWords = len(withoutPunctuation.split())
        for word in withoutPunctuation.split():
            if not word.isalpha():
                break
            if termsDb.contains(where('term') == word):
                knownWords += 1
        translation = self.textEdit_translation.toPlainText()
        currLang = self.comboBox_languages.currentText()
        row = {}                                                # TODO: check if not duplicate
        row['language'] = currLang
        row['sentence'] = sentence
        row['translation'] = translation
        row['totalWords'] = totalWords
        row['TODOs'] = totalWords - knownWords
        sentencesDb.insert(row)

    def selChanged(self):
        cursor = self.textEdit_sentence.textCursor()
        beginPos = cursor.selectionStart()
        endPos = cursor.selectionEnd()
        if beginPos != endPos:
            wholeText = self.textEdit_sentence.toPlainText()
            selectedText = wholeText[beginPos:endPos]
            print(selectedText)

# databases
languagesDb = TinyDB('data/languages.json')
sentencesDb = TinyDB('data/sentences.json')
termsDb = TinyDB('data/terms.json')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LwsMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
