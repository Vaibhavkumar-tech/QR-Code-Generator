import qrcode as qr
m=input("enter")
image=qr.make(m)
image.save("Linkedin.png")