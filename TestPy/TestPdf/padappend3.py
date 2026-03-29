from PyPDF2 import PdfWriter

merger = PdfWriter()

input1 = open("D:\\NotePC\\探亲签证\\1_理由书.pdf", "rb")
input2 = open("D:\\NotePC\\探亲签证\\1_申請人名簿.pdf", "rb")
input3 = open("D:\\NotePC\\探亲签证\\1_招へい経緯書.pdf", "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 1))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("D:\\NotePC\\探亲签证\\temp\\document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()