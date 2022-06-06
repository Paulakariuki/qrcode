import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
url = print(input("Enter the link you'd like to generate:\n"))
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
type(img)  # qrcode.image.pil.PilImage
img.save(url.to_str()+".png")