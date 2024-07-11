#  Encoding

import qrcode

img = qrcode.make('https://www.linkedin.com/in/hamza-meer')

img.save('Qr.png')


# Decoding

import cv2

img = cv2.imread('Qr.png')
data = cv2.QRCodeDetector()
v1 = data.detectAndDecode(img)

print(v1[0])

