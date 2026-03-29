import PyPDF2
import sys
import os
  
merger = PyPDF2.PdfMerger()
  
for file in os.listdir("D:\\NotePC\\探亲签证\\"):
    
    if file.endswith(".pdf"):
        print(file)
        merger.append("D:\\NotePC\\探亲签证\\" + file)
  
merger.write("D:\\NotePC\\探亲签证\\temp\\combined.pdf")