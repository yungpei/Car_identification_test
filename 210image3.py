from PIL import Image
img = Image.open("pic\\example.png")

imggray = img.convert('L')      # 轉換為灰階

imggray.save("pic\\gray01.png")

imggray.show()