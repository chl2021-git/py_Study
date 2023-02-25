from contextlib import nullcontext
import os
import difflib
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
def getLineList(filepath,fileNM):

    lst = []
    f = open(filepath + fileNM, mode='r') 

    for lineF in f.readlines():
        lst.append(lineF)

    f.close()
    return(lst)
#
folder  = 'D:\Study\py_Study\TestPy\\diff_date\\work\\'
lineLst = getLineList(folder, '2.txt')

f1 = open(folder + '1.txt', mode='r') 
fw = open(folder + 'out1.txt', mode='w' ,encoding='UTF-8')
lineCnt = 0
for lineF in f1.readlines():
    lineCnt = lineCnt + 1
    ret = difflib.get_close_matches(lineF , lineLst, n=2 ,cutoff=0.95)
    print(ret)

    fw.write('key:' + lineF )
    if len(ret) == 0:
        fw.write('not found %d \n' %( lineCnt))
    else:
         fw.write('mat:' + ret[0] )

f1.close()
fw.close()

