import os
import re
#
count_re = 0
#
def getFile(filepath):
    lst = []
    files = os.listdir(filepath)  
    for fl in os.listdir(filepath)  :
        if os.path.isfile(filepath + fl):
            lst.append(fl)
    print(lst)
    return  lst
#
def writeFile(filepath,fileLst):
    for fl in fileLst:
        f = open(filepath + fl, mode='r',encoding='UTF-8') 
        fw = open(filepath + '\\wk\\wk-' + fl , mode='w' ,encoding='UTF-8')
        count = 0

        for lineF in f.readlines():
            count = count + 1
            findLine(lineF) 
        fw.close()
        f.close()
        global count_re
        print('count=%d / %d lines' % (count_re, count))

    return
#
#
def findLine(line):
    matchObj = re.findall(r'(｜(.*?)《(.*?)》)', line)
    if matchObj:
        for m in matchObj:
            print(m)
            global count_re
            count_re +=  1
        return ''
    else:
        return line
#
print('start....')
fileList = getFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\')
writeFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\',fileList)
