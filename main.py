import qrcode
f = open('work.txt', 'r')
qn = 0
for line in f:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=30,
        border=4,
    )
    qn += 1
    qr.add_data(line)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(+str(qn)+".png")
