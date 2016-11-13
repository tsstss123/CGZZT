try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication, QPushButton, QLabel)
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

try:
    import _pickle as cPickle
    import urllib.request as url
except ImportError:
    import cPickle
    import urllib as url

import sys
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
        if sys.version > '3':
            super().__init__()
        else:
            super(QWidget, self).__init__()
        self.initUI()


    def initUI(self):

        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        btn1 = QPushButton("RIGHT", self)
        btn2 = QPushButton("WRONG", self)
        btn3 = QPushButton("W T F", self)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.picLabel = QLabel(self)
        # self.picLabel.setPixmap(QPixmap('temp.jpg'))
        self.picLabel.setAlignment(Qt.AlignCenter)
        self.ansLabel = QLabel(self)
        self.ansLabel.setAlignment(Qt.AlignCenter)

        font_20pix = QFont()
        font_20pix.setPixelSize(20)
        font_48pix = QFont()
        font_48pix.setPixelSize(48)

        btn1.setFont(font_20pix)
        btn2.setFont(font_20pix)
        btn3.setFont(font_20pix)
        self.label.setFont(font_20pix)
        self.ansLabel.setFont(font_48pix)


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

        self.renewtext()
        self.show()

    def renewtext(self):
        if (self.sCnt + self.fCnt > 0):
            self.label.setText("%2.0f%% in %d pic" % (100.0 * self.sCnt / (self.sCnt + self.fCnt), self.sCnt + self.fCnt))
        pullPic('temp.jpg')
        if sys.version > '3':
            self.picLabel.setPixmap(QPixmap('temp.jpg').scaled(200,80))
        else:
            oimg = cv2.imread('temp.jpg')
            cv2.imwrite('temp.png', oimg)
            self.picLabel.setPixmap(QPixmap('temp.png').scaled(200,80))
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
    url.urlretrieve(webpath, path)

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
    print(np.amax(prob,axis = 1)) 
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
    return ' '.join(ans)
    


if __name__ == '__main__':
    pullPic('temp.jpg')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
