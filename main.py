from PyQt5 import QtWidgets
import sys
from calculator import Ui_MainWindow
from __init__ import var


class myApp(QtWidgets.QMainWindow,var):

    def __init__(self):
        super(myApp, self).__init__()
        super(myApp, self)
        
    def number(self):
        if self.operationNumber=="+" or self.operationNumber=="-":
            self.ui.mainText.setText("0")
            self.operationNumber=""
        if self.operationNumber=="*" or self.operationNumber=="/" or self.operationEqual=="=":
            self.ui.mainText.setText("")
            self.operationNumber=""
        if self.ui.mainText.toPlainText()=="0":
            self.ui.mainText.setText("")
        self.ui.mainText.setText(self.ui.mainText.toPlainText()+self.sender().text())

    def clean(self):
        self.ui.mainText.setText("0")
        self.result=0
        self.givenNumber=0
        self.firstControl=0
        self.operationEqual=""
        self.operation=""
        self.operationNumber=""

    def equal(self):
        if self.firstControl==0:
            self.givenNumber=self.ui.mainText.toPlainText()
            self.givenNumber=int(self.givenNumber)
            self.result= self.givenNumber
            self.ui.mainText.setText(str(self.result))
            self.firstControl=1
        else:
            if self.operationEqual=="+":
                self.givenNumber=self.ui.mainText.toPlainText()
                self.intFloatControl()
                self.result= self.result+self.givenNumber
                self.ui.mainText.setText(str(self.result))
                self.givenNumber=0
            if self.operationEqual=="-":
                self.givenNumber=self.ui.mainText.toPlainText()
                self.intFloatControl()
                self.result= self.result - self.givenNumber
                self.ui.mainText.setText(str(self.result))
                self.givenNumber=0
            if self.operationEqual=="*":    
                self.givenNumber=self.ui.mainText.toPlainText()
                self.intFloatControl()
                self.result= self.result * self.givenNumber
                self.ui.mainText.setText(str(self.result))
                self.givenNumber=0
            if self.operationEqual=="/":    
                self.givenNumber=self.ui.mainText.toPlainText()
                self.intFloatControl()
                self.result= self.result / self.givenNumber
                self.intFloatControl()
                self.ui.mainText.setText(str(self.result))
                self.givenNumber=0 
        if self.sender().text()=="=":
            self.operationEqual="="
            self.firstControl=0

    def intFloatControl(self):
        if int(self.result)==float(self.result):
            self.result=int(self.result)
        else:
            self.result=float(self.result)
        if int(self.givenNumber)==float(self.givenNumber):
            self.givenNumber=int(self.givenNumber)
        else:
            self.givenNumber=float(self.givenNumber)

    def plus (self):
        self.equal() 
        self.operationEqual="+"
        self.operation="+"
        self.operationNumber="-"

    def sub (self):
        self.equal()
        self.operationEqual="-"
        self.operation="-"
        self.operationNumber="-"
        

    def mul (self):
        self.equal()
        self.operationEqual="*" 
        self.operation="*"
        self.operationNumber="*"

    def div (self):
        self.equal()
        self.operationEqual="/" 
        self.operation="/"
        self.operationNumber="/"

    def changeColors(self,*arg):
        self.ui.pushButton_clean.setStyleSheet(self.whichColor)
        self.ui.pushButton_0.setStyleSheet(self.whichColor)
        self.ui.pushButton_1.setStyleSheet(self.whichColor)
        self.ui.pushButton_2.setStyleSheet(self.whichColor)
        self.ui.pushButton_3.setStyleSheet(self.whichColor)
        self.ui.pushButton_4.setStyleSheet(self.whichColor)
        self.ui.pushButton_5.setStyleSheet(self.whichColor)
        self.ui.pushButton_6.setStyleSheet(self.whichColor)
        self.ui.pushButton_7.setStyleSheet(self.whichColor)
        self.ui.pushButton_8.setStyleSheet(self.whichColor)
        self.ui.pushButton_9.setStyleSheet(self.whichColor)
        self.ui.pushButton_plus.setStyleSheet(self.whichColor)
        self.ui.pushButton_sub.setStyleSheet(self.whichColor)
        self.ui.pushButton_mul.setStyleSheet(self.whichColor)
        self.ui.pushButton_div.setStyleSheet(self.whichColor)
        self.ui.pushButton_clean.setStyleSheet(self.whichColor)
        self.ui.pushButton_equal.setStyleSheet(self.whichColor)
        self.ui.mainText.setStyleSheet(self.whichColor)

    def color(self):
        getText=self.sender().text()
        if getText=="Pink":
            self.whichColor="background-color: pink; color:yellow; border:10px;"
            self.changeColors(self.whichColor)
        if getText=="Red":
            self.whichColor="background-color: red; color:green; border:10px;"
            self.changeColors.changeColors(self.whichColor)
        if getText=="Black":
            self.whichColor="background-color: black; color:white; border:10px;"
            self.changeColors(self.whichColor)
        if getText=="Blue":
            self.whichColor="background-color: blue; color:orange; border:10px;"
            self.changeColors(self.whichColor)
        if getText=="Grey":
            self.whichColor="background-color: grey; color:black; border:10px;"
            self.changeColors(self.whichColor)
        if getText=="White":
            self.whichColor="background-color: white; color:black; border:10px;"
            self.changeColors(self.whichColor)

def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton {border-radius:10px; background-color: black; color:white; border:10px;}")
    win = myApp()
    win.show()
    sys.exit(app.exec_())
    

app()

    