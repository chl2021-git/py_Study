
import os
from PIL import Image
import pyocr
 
#インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
#OS自体に設定してあれば以下の2行は不要
path='D:\\Program Files\\Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path
 
#pyocrへ利用するOCRエンジンをTesseractに指定する。
pyocr.tesseract.TESSERACT_CMD = r'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
 
#OCR対象の画像ファイルを読み込む
img = Image.open("D:\\Study\\py_Study\\TestPy\\img\\test3.png")
 
#画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
#text = tool.image_to_string(img, lang="jpn_vert", builder=builder)
text = tool.image_to_string(img, lang="jpn_vert")
 
print(text)