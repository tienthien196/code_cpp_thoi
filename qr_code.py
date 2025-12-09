import qrcode


img = qrcode.make("hello tiến thiện")

img.save(r"./img_code.png")
img.show()