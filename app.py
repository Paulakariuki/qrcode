import qrcode
import os. path
import time as time

def shop():
    
    print("=========================\n")
    count = int(input("Enter the number of shops you'd like to generate the QR code/s for:\n"))
    # Working with a for loop to iterate over the process based on the input above 
    for x in range(count):
        # initialize qr code library
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        # prompt user to key in the value they would like to serialize using qr  
        url = input("Enter the link you'd like to generate:\n")
        shop = input("Enter the name of the vendor/shop:\n")
        sanitize = "https://"+url
        print(sanitize)
        qr.add_data(sanitize)
        qr.make(fit=True)
        # You can change the color of the files
        img = qr.make_image(fill_color="#0a3d62", back_color="white")
        type(img)  # qrcode.image.pil.PilImage
        # Save the image
        img.save('images/'+shop+'.jpg')
        print("==========================\n")
        print("QR code generated for " + shop + "\n")
        print("==========================")

shop()