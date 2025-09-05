from PIL import Image
img = Image.open("pic\\example.png")

w,h = img.size      # 750, 750

img1 = img.resize((w*2, h))
img1.save("pic\\resize01.png")

img1.show()