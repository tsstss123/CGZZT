from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QLabel)

import sys
import _pickle as cPickle
import urllib.request

import mxnet as mx
import numpy as np
import cv2
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

model_name = 'inception-tan-v2'

mod = mx.model.FeedForward.load(model_name,14)

f = open('char.pki','rb')
chdst = cPickle.load(f)

class Example(QWidget):
    sCnt = 0
    fCnt = 0
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        btn1 = QPushButton("Yes", self)
        btn2 = QPushButton("No", self)
        btn3 = QPushButton("WTF", self)
        self.label = QLabel(self)
        self.picLabel = QLabel(self)
        self.picLabel.setPixmap(QPixmap('temp.jpg'))
        self.ansLabel = QLabel(self)


        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(self.label)
        vbox.addWidget(self.picLabel)
        vbox.addWidget(self.ansLabel)

        self.setLayout(vbox)
        btn1.clicked.connect(self.YesClick)
        btn2.clicked.connect(self.NoClick)
        btn3.clicked.connect(self.WTFClick)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Predict')
        self.show()

    def renewtext(self):
        self.label.setText("%2.0f%% in %d pic" % (100.0 * self.sCnt / (self.sCnt + self.fCnt), self.sCnt + self.fCnt))
        pullPic('temp.jpg')
        self.picLabel.setPixmap(QPixmap('temp.jpg'))
        ans = Predict()
        self.ansLabel.setText(ans)
        
    def YesClick(self):
        self.sCnt = self.sCnt + 1
        self.renewtext()

    def NoClick(self):
        self.fCnt = self.fCnt + 1
        self.renewtext()

    def WTFClick(self):
    	self.renewtext()




webpath = r'http://cab2b.travelsky.com/cab2b/VerificationCode.do'

def pullPic(path):
    urllib.request.urlretrieve(webpath, path)

def predictSingle(pic):
    assert(pic.shape == (40,40,3))
    r = pic[:,:,0]
    g = pic[:,:,1]
    b = pic[:,:,2]
    bp = np.zeros((3,40,40))
    bp[0,:,:] = r
    bp[1,:,:] = g
    bp[2,:,:] = b
    bp.shape = (1,3,40,40)
    bp = bp.astype(np.float32)/255
    dataiter = mx.io.NDArrayIter(bp)
    prob = mod.predict(dataiter)
    # print prob
    py = np.argmax(prob,axis = 1) 
    id = py[0]
    print(id)
    for (ch,idx) in chdst.items():
    	if(idx == id):
    		return ch
    return None

def Predict():
    src = cv2.imread('temp.jpg')
    assert(src.shape == (40,100,3))
    one = src[0:40,0:40,:]
    two = src[0:40,30:70,:]
    three = src[0:40,60:100,:]
    ans = [predictSingle(one),predictSingle(two),predictSingle(three)]
    return str(ans)
    


if __name__ == '__main__':
    pullPic('temp.jpg')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
