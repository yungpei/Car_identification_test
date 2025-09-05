from PIL import Image, ImageDraw
from PIL import ImageFont

img = Image.new("RGB", (300, 400), "lightgray")
drawing = ImageDraw.Draw(img)

# 繪圖
drawing.ellipse((50,50,250,250), width = 3, outline = "gold")   # 臉

# 繪多邊形
drawing.polygon([(100,90),(120,130),(80,130)], fill = "brown", outline = "red")     # 左眼睛
drawing.polygon([(200,90),(220,130),(180,130)], fill = "brown", outline = "red")    # 右眼睛

# 繪矩形
drawing.rectangle((140, 140, 160, 180), fill = "blue", outline = "black")           # 鼻子

# 繪橢圓
drawing.ellipse((100, 200, 200, 220), fill = "red")                                 # 嘴巴

# 文字
drawing.text((130, 280), "e-happy", fill = "orange")
myfont = ImageFont.truetype("C:/Windows/Fonts/msjhbd.ttc", 16)

drawing.text((80, 320), "我想下班，不想上班", fill = "red", font = myfont)

img.show()
img.save("pic\\happyface.png")