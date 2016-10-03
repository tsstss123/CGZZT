# -*- coding: utf-8 -*-

from os import walk
import cPickle

def get_all_dir_files():
    f = []
    for (dirpath, dirnames, filenames) in walk('.'):
        f.extend(filenames)
        break
    return f

if __name__ == '__main__':
    opt = open("static.txt","w")
    files = get_all_dir_files()
    cal = {}
    allch = []
    chsum = 0
    catlog = 0
    for fname in files:
        sfx = fname.split('.')[1]
        if sfx == 'jpg' or sfx == 'png' or sfx == 'jpeg':
            name = fname.split('.')[0].decode('GB2312')
            for ch in name:
                if ch not in cal:
                    allch.append(ch)
                    cal[ch] = 1
                    catlog += 1
                else:
                    cal[ch] += 1
                chsum += 1
    opt.write("%d sample, %d chars\n" % (chsum, catlog))
    for (k,v) in cal.items():
        opt.write("%s -- %2d times,  %.2f%%\n" % (k.encode('GB2312'), v , 100.0 * v / chsum))
    f = open('char.pki','w')
    cPickle.dump(allch,f)
