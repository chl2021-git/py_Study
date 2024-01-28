f = open('D:\\Study\\py_Study\\TestPy\\test_f\\all.txt' , mode='r',encoding='UTF-8') 
fw = open('D:\\Study\\py_Study\\TestPy\\test_f\\all_out.txt' , mode='a+',encoding='UTF-8') 
for lineF in f.readlines():
    fw.write( "<p>" + lineF + "<//p>" )
fw.close()
f.close