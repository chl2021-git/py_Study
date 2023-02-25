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
        fw = open(filepath + '\\wk\\wk-' + fl , mode='w' ,encoding='UTF-8')
        for lineF in f.readlines():
                    fw.write(changeLine(lineF) )
        fw.close()
        f.close()
    return
#
def skipLine(line):
    matchObj = re.match(r'［＃.*］', line)
    if matchObj:
        #print(matchObj.group(0))
        return ''
    else:
        return line
#
def changeLine(line):
    changedict = {'［＃.*］': '', 
                  '｜': '<ruby class="pcalibre2 pcalibre1"><rb class="pcalibre2 pcalibre1">', 
                  '《': '</rb><rt class="pcalibre2 pcalibre1">',
                  '》': '</rt></ruby>'}
    for key,values in  changedict.items():
        line = re.sub(key, values, line)
    #content1 = re.sub(r'［＃.*］', '', line)
    #content2 = re.sub(r'｜', '<ruby class="pcalibre2 pcalibre1"><rb class="pcalibre2 pcalibre1">', content1)
    #content3 = re.sub(r'《', '</rb><rt class="pcalibre2 pcalibre1">', content2)
    #content4 = re.sub(r'》', '</rt></ruby>', content3)

    return line
#
print('start....')
fileList = getFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\')
writeFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\',fileList)
