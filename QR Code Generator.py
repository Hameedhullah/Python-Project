#Importing the libraries
import qrcode
from PIL import Image

#Creating Qrcode
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 15, border = 4)
qr.add_data('https://www.cricbuzz.com/')
qr.make(fit = True)

# Saving the Qrcode image in file path
img = qr.make_image()
img.save("cricket.png")
