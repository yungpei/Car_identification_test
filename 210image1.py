from PIL import Image
img = Image.open("pic\\example.png")

img.show()
w,h = img.size
print(w, h)

filename = img.filename
print(filename)