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
        f = open(filepath + 'work\\' + fl, mode='r',encoding='UTF-8') 
        fw = open(filepath + 'work2\\' + fl, mode='w' ,encoding='UTF-8')

        content = f.read()
  
        content0 = re.sub(r'\n正确答案\n', '\n正确答案：', content)
        content1 = re.sub(r'\nA\n', '\nA：', content0)
        content2 = re.sub(r'\nB\n', '\nB：', content1)
        content3 = re.sub(r'\nC\n', '\nC：', content2)
        content4 = re.sub(r'\nD\n', '\nD：', content3)
        content5 = re.sub(r'\nE\n', '\nE：', content4)
        content6 = re.sub(r'\nF\n', '\nF：', content5)
        content7 = re.sub(r'\n解析：\n暂无解析\n', '\n', content6)
        #print(content7)

        fw.write(content7)
        fw.close()
        f.close()
    return
#
fileList = getFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\')
writeFile('D:\Study\py_Study\TestPy\FormatFileToAzw\\',fileList)
