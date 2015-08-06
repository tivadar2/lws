class MenuBar:
    def __init__(self, stackedWidget):
        self.stackedWidget_main = stackedWidget

    def changeToAddSentence(self):
        self.stackedWidget_main.setCurrentIndex(0)

    def changeToAddLanguage(self):
        self.stackedWidget_main.setCurrentIndex(1)

    def changeToViewTerms(self):
        self.stackedWidget_main.setCurrentIndex(2)
        
    def changeToViewSentences(self):
        self.stackedWidget_main.setCurrentIndex(3)
