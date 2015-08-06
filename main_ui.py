# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 591, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 241, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 30, 241, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_sentence = QtWidgets.QLabel(self.tab)
        self.label_sentence.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_sentence.setObjectName("label_sentence")
        self.label_translation = QtWidgets.QLabel(self.tab)
        self.label_translation.setGeometry(QtCore.QRect(260, 10, 61, 21))
        self.label_translation.setObjectName("label_translation")
        self.pushButton_addSentence = QtWidgets.QPushButton(self.tab)
        self.pushButton_addSentence.setGeometry(QtCore.QRect(210, 80, 101, 23))
        self.pushButton_addSentence.setObjectName("pushButton_addSentence")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(10, 10, 291, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 81, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_addLang = QtWidgets.QPushButton(self.frame)
        self.pushButton_addLang.setGeometry(QtCore.QRect(184, 100, 91, 23))
        self.pushButton_addLang.setObjectName("pushButton_addLang")
        self.lineEdit_language = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_language.setGeometry(QtCore.QRect(90, 30, 161, 20))
        self.lineEdit_language.setObjectName("lineEdit_language")
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox_languages = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_languages.setGeometry(QtCore.QRect(120, 10, 151, 22))
        self.comboBox_languages.setObjectName("comboBox_languages")
        self.label_currLang = QtWidgets.QLabel(self.centralwidget)
        self.label_currLang.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_currLang.setObjectName("label_currLang")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Learning with Sentences"))
        self.pushButton.setText(_translate("MainWindow", "get from tatoeba"))
        self.label_sentence.setText(_translate("MainWindow", "Sentence"))
        self.label_translation.setText(_translate("MainWindow", "Translation"))
        self.pushButton_addSentence.setText(_translate("MainWindow", "Add sentence"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Sentence"))
        self.label.setText(_translate("MainWindow", "Study Languge:"))
        self.label_2.setText(_translate("MainWindow", "New Language"))
        self.pushButton_addLang.setText(_translate("MainWindow", "Add language"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Languages"))
        self.label_currLang.setText(_translate("MainWindow", "Current language:"))

