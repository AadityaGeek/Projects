import qrcode
import os

#version decides the higher number create larger codes
#box_size decides storage size of qr
#border decides distance from all sides
features=qrcode.QRCode(version=1,box_size=50,border=5)

qr_data=input("Enter text for QR Code: ")
#qr_data='https://linkt.ree/aaditykr_'

features.add_data(qr_data)
#fit=True change the version of qr according to data
features.make(fit=True)

#change color of qr code
generate_image=features.make_image(fill_color="black",back_color="white")

base_filename='image_1.png'
filename=base_filename
counter=1
while os.path.exists(filename):
    filename=f"image_{counter}.png"
    counter+=1
#Save qr as image
generate_image.save(filename)

#Show success message
print(f"QR Code generated Successfully! Saved as {filename}")
