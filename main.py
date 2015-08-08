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
        self.pushButton_addTerm.clicked.connect(self.addTerm)
        self.textEdit_sentence.selectionChanged.connect(self.selChanged)
        self.tableWidget_sentences.currentCellChanged.connect(self.chooseSentence)
        self.textEdit_currSentence.selectionChanged.connect(self.chooseTerm)

        # menu bar bindings
        self.action_addSentence.triggered.connect(self.menuBar.changeToAddSentence)
        self.action_addLanguage.triggered.connect(self.menuBar.changeToAddLanguage)
        self.action_viewTerms.triggered.connect(self.menuBar.changeToViewTerms)
        self.action_viewSentences.triggered.connect(self.menuBar.changeToViewSentences)
        self.action_viewSentences.triggered.connect(self.updateTableSentences)

        # setup tableWidget_terms
        headers = ['Term', 'Translation', 'Score']
        self.tableWidget_terms.setColumnCount(3)
        self.tableWidget_terms.setHorizontalHeaderLabels(headers)

        # setup tableWidget_sentences
        headers = ['Sentence', 'Translation', 'Total Words', 'Unknown words']
        self.tableWidget_sentences.setColumnCount(4)
        self.tableWidget_sentences.setHorizontalHeaderLabels(headers)
        self.updateTableSentences()
        
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

    def addTerm(self):
        term = self.lineEdit_term.text()
        translation = self.lineEdit_termTranslation.text()
        if not termsDb.contains(where('term') == term):
            row = {}
            row['term'] = term
            row['translation'] = translation
            termsDb.insert(row)
            print('Term succesfully added!')
            for row in sentencesDb.all():
                withoutPunctuation = ''.join(c for c in row['sentence'].lower() if c not in string.punctuation)
                if term in withoutPunctuation.split():
                    TODOs = sentencesDb.get(eid=row.eid)['TODOs']
                    sentencesDb.update({'TODOs': TODOs-1}, where('sentence') == row['sentence'])
        else:
            print('Term is already in the database!')

    def selChanged(self):
        cursor = self.textEdit_sentence.textCursor()
        beginPos = cursor.selectionStart()
        endPos = cursor.selectionEnd()
        if beginPos != endPos:
            wholeText = self.textEdit_sentence.toPlainText()
            selectedText = wholeText[beginPos:endPos]
            print(selectedText)

    def chooseSentence(self, row, column):
        sentence = self.tableWidget_sentences.item(row, 0).text()
        self.textEdit_currSentence.setText(sentence)

    def chooseTerm(self):
        cursor = self.textEdit_currSentence.textCursor()
        beginPos = cursor.selectionStart()
        endPos = cursor.selectionEnd()
        if beginPos != endPos:
            wholeText = self.textEdit_currSentence.toPlainText()
            selectedText = wholeText[beginPos:endPos]
            self.lineEdit_term.setText(selectedText.lower())

    def updateTableSentences(self):
        allSentences = sentencesDb.all()
        self.tableWidget_sentences.setRowCount(len(allSentences))
        row = 0
        for sentence in allSentences:
            self.tableWidget_sentences.setItem(row, 0, QtWidgets.QTableWidgetItem(sentence['sentence']))
            self.tableWidget_sentences.setItem(row, 1, QtWidgets.QTableWidgetItem(sentence['translation']))
            self.tableWidget_sentences.setItem(row, 2, QtWidgets.QTableWidgetItem(str(sentence['totalWords'])))
            self.tableWidget_sentences.setItem(row, 3, QtWidgets.QTableWidgetItem(str(sentence['TODOs'])))
            row += 1
        

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
