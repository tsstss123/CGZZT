import cv2
import numpy as np
import mxnet as mx
from os import walk
import argparse

def get_all_dir_files():
    f = []
    for (dirpath, dirnames, filenames) in walk('.'):
        f.extend(filenames)
        break
    return f

def guass(image_path):
    src = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    # Reverse black and write
    src = 255 - src
    # threshold
    retval, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY)
    return dst

def crop(img):
    a = img[10:45,33:54]
    b = img[10:45,54:78]
    c = img[10:45,78:102]
    d = img[10:45,102:122]
    a = norm(a)
    b = norm(b)
    c = norm(c)
    d = norm(d)
    return [a,b,c,d]

def norm(img):
    ylen = (35 - img.shape[1]) / 2
    res = np.zeros((35,35),dtype = np.uint8)
    res[:,ylen:ylen + img.shape[1]] = img
    res = cv2.resize(res,(28,28))
    return res

def load_model():
    return mx.model.FeedForward.load('inception-bn-28',22)

def predict_pic(mod,im):
    # im = cv2.imread(path,color_modes[0])
    assert(im.shape == (28,28))
    im.shape = (1,1,28,28)
    dataiter = mx.io.NDArrayIter(
        im)
    prob = mod.predict(dataiter)
    # print prob
    py = np.argmax(prob,axis = 1)
    # print 'predict ans = ', py[0]
    return py[0]

def predict(mod,name):
    res = guass(name)
    four_pic = crop(res)
    ans = []
    for i in range(4):
        ret = predict_pic(mod,four_pic[i])
        if ret >= 10:
            ans.append(chr(ret - 10 + ord('A')))
        else:
            ans.append(chr(ret + ord('0')))
    return ans

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-file',type=str,default='',help='Picture name')
    args = parser.parse_args()

    mod = load_model()
    if args.file == '' or args.file == None:
        sucscnt = 0
        failcnt = 0
        files = get_all_dir_files()
        for fname in files:
            if len(fname.split('.')) != 2:
                continue
            prefix, suffix = fname.split('.')
            if suffix != 'png' and suffix != 'jpg':
                continue
            if len(prefix) != 4:
                continue
            strlist = predict(mod,fname)
            ans = ''.join(strlist)
            if ans.upper() == prefix.upper():
                sucscnt += 1
                print(fname + " pass")
            else:
                failcnt += 1
                print(fname + " fail")

        print("%.2f passed" % (sucscnt * 1.0 / (sucscnt + failcnt)))
    else:
        ans = predict(mod,args.file)
        print("%c%c%c%c" % (ans[0],ans[1],ans[2],ans[3]))
