
import qrcode as qr
from PIL import Image
qr=qr.QRCode(version=1, box_size=10, border=5,error_correction=qr.constants.ERROR_CORRECT_H)
qr.add_data("https://www.linkedin.com/in/vaibhav-kumar-729209311/")
qr.make(fit=True)
image=qr.make_image(fill_color="blue",back_color="white")
image.save("Linkedin.png")