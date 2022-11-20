import pyqrcode
from pyqrcode import QRCode

s=input("Enter information :")
name=input("Enter the name of your qr code with .svg ")
url=pyqrcode.create(s)

url.svg(name,scale=8)