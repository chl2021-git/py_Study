import os
import re
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
def writeFile(filepath,fileNM):

    f = open(filepath + fileNM, mode='r') 
    fw = open(filepath + 'work\\' + fileNM, mode='w' ,encoding='UTF-8')
    
    content = ''
    contentFlg = 0
    for lineF in f.readlines():
        if ('题' in lineF) :
            contentFlg = 1
            content = ''
            continue
        if contentFlg == 1:
            if ('A.' == lineF[:2] or 'A：' == lineF[:2]) :
                contentFlg = 0
                content = content.replace('\n' ,' ')
                print(content + '\n')
                fw.write(content +  '\n')
            else:
                content = content + lineF
    #fw.write(findContent)
    fw.close()
    f.close()
####
writeFile('D:\Study\py_Study\TestPy\\diff_date\\', '2.txt')

