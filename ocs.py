import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'F://Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('F://ocs/1.png'))

print(type(text))
print(text)
