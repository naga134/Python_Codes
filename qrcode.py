import pyqrcode
from PIL import Image
link = input("Enter the link: ")
qrcode = pyqrcode.create(link)
qrcode.png('QRcode.png', scale=6)
Image.open('QRcode.png')