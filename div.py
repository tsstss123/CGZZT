# -*- coding: utf-8 -*-
import cv2
import numpy as np
import cPickle as pickle
from os import walk

def get_all_dir_files():
    f = []
    for (dirpath, dirnames, filenames) in walk('.'):
        f.extend(filenames)
        break
    return f

def guass(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    print img.shape
    for x in range(0,img.shape[0]):
        for y in range(0,img.shape[1]):
            if img[x][y] > 130:
                img[x][y] = 0
            else:
                img[x][y] = 255 - img[x][y]
    return img

def crop(img):
    a = img[:,0:35]
    b = img[:,30:65]
    c = img[:,60:95]
    return [a,b,c]

dir_prefix = 'chinese/'
lst_file = open('opt.lst','w')
lst_item_count = 1

def write_list(filename,idx):
    global lst_item_count
    lst_file.write('%d\t%d\t%s' % (lst_item_count, idx, dir_prefix + filename))
    lst_item_count += 1

if __name__ == '__main__':

    array_file = open('../char.pki','r+')
    chars = pickle.load(array_file)
    array_file.close()
    # 装载字符编号(gb2312格式)

    files = get_all_dir_files()
    for fname in files:
        if fname.split('.')[1] == 'jpg':
            chs = fname.decode('GB2312').split('.')[0] # 解码文件名并判断合法性
            if len(chs) != 3:
                continue
            imgs = crop(guass(fname)) # 分割图片
            ids = [chars[chs[0]],chars[chs[1]],chars[chs[2]]] # 转换为编号
            for i in range(3):
                outputname = str(lst_item_count) + '-' + str(ids[i]) + '.png'
                write_list(outputname,ids[i])
                cv2.imwrite(outputname,imgs[i])
