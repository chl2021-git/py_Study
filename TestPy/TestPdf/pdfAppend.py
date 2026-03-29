from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["1_理由书.pdf",
            "1_申請人名簿.pdf",
            "1_招へい経緯書.pdf",
            "2_滞在予定表.pdf",
            "3ac_住民票.pdf",
            "3b1_受信通知.pdf",
            "3b2_確定申告書.pdf",
            "3d_身元保証書.pdf"]:
    merger.append("D:\\NotePC\\探亲签证\\" + pdf)

merger.write("D:\\NotePC\\探亲签证\\temp\\merged-pdf.pdf")
merger.close()