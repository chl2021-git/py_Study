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
def writeFile(filepath,fileLst):
    for fl in fileLst:
        f = open(filepath + fl, mode='r',encoding='UTF-8') 
        fw = open(filepath + fl + '-1', mode='w' ,encoding='UTF-8')
        for lineF in f.readlines():
            if skipLine(lineF.strip()) != "":
                fw.write(lineF )
        fw.close()
        f.close()
    return
#
def skipLine(line):
    matchObj = re.match(r'(你的选择)|(难易度)|(返回)|(\w+一题)|(（1分）)', line)
    if matchObj:
        print(matchObj.group(0))
        return ''
    else:
        return line
#
fileList = getFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\')
writeFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\',fileList)
