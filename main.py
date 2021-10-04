import qrcode

def qr_generate(url, saved_img = 'QrCode.png'):
    img = qrcode.make(url)
    img.save(saved_img)
    return img

url = "https://techfandome2020.netlify.app/"
qr_generate(url)