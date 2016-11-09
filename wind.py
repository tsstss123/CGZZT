import sys
import pickle
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QLabel)


class Example(QWidget):
    sCnt = 0
    fCnt = 0
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        btn1 = QPushButton("Yes",self)
        btn2 = QPushButton("No", self)
        self.label = QLabel(self)
        self.picLabel = QLabel(self)
        self.picLabel.setPixmap(QPixmap('temp.jpg'))

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(self.label)
        vbox.addWidget(self.picLabel)

        self.setLayout(vbox)
        btn1.clicked.connect(self.YesClick)
        btn2.clicked.connect(self.NoClick)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def renewtext(self):
        self.label.setText("%2.0f%% in %d pic" % (100.0 * self.sCnt / (self.sCnt + self.fCnt), self.sCnt + self.fCnt))
        pullPic('temp.jpg')
        self.picLabel.setPixmap(QPixmap('temp.jpg'))
        
    def YesClick(self):
        self.sCnt = self.sCnt + 1
        self.renewtext()

    def NoClick(self):
        self.fCnt = self.fCnt + 1
        self.renewtext()

webpath = r'http://cab2b.travelsky.com/cab2b/VerificationCode.do'

def pullPic(path):
    urllib.request.urlretrieve(webpath, path)

if __name__ == '__main__':
    pullPic('temp.jpg')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
