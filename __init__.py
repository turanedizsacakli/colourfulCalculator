from PyQt5 import QtWidgets
import sys
from calculator import Ui_MainWindow

class var:
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.result=0
        self.givenNumber=0
        self.operation=""
        self.operationEqual=""
        self.operationNumber=""
        self.ui.mainText.setText("0")
        self.whichColor=""
        self.firstControl=0
        self.ui.pushButton_0.clicked.connect(self.number)
        self.ui.pushButton_1.clicked.connect(self.number)
        self.ui.pushButton_2.clicked.connect(self.number)
        self.ui.pushButton_3.clicked.connect(self.number)
        self.ui.pushButton_4.clicked.connect(self.number)
        self.ui.pushButton_5.clicked.connect(self.number)
        self.ui.pushButton_6.clicked.connect(self.number)
        self.ui.pushButton_7.clicked.connect(self.number)
        self.ui.pushButton_8.clicked.connect(self.number)
        self.ui.pushButton_9.clicked.connect(self.number)
        self.ui.pushButton_plus.clicked.connect(self.plus)
        self.ui.pushButton_sub.clicked.connect(self.sub)
        self.ui.pushButton_mul.clicked.connect(self.mul)
        self.ui.pushButton_div.clicked.connect(self.div)
        self.ui.pushButton_clean.clicked.connect(self.clean)
        self.ui.pushButton_equal.clicked.connect(self.equal)
        self.ui.actionPink.triggered.connect(self.color)
        self.ui.actionGrey.triggered.connect(self.color)
        self.ui.actionBlack.triggered.connect(self.color)
        self.ui.actionBlue.triggered.connect(self.color)
        self.ui.actionRed.triggered.connect(self.color)
        self.ui.actionWhite.triggered.connect(self.color)
