import qrcode

#Simple QR code
data_input=input("Enter your text to create QR code: ")
qr_data=qrcode.make(data_input)
qr_data.save('image1.png')
print("QR Code generated Successfully!")
