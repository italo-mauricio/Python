import qrcode



data = 'dont\'t forget to subscribe'

img = qrcode.make(data)

img.save('C:/Users/italo/Documents/qr code/myqrcode.png')