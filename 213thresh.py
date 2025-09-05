import cv2
from PIL import Image

gray = cv2.imread("detect\\face1.jpg", 0)                       # 以灰階模式開啟圖片
_,thresh = cv2.threshold(gray, 187, 255, cv2.THRESH_BINARY)     # 轉為黑白
cv2.imwrite("pic\\thresh1.jpg", thresh)                         # 存檔

img = Image.open('detect\\face1.jpg')
w, h = img.size
img = img.convert('L')                                          # 先轉為灰階
for i in range(w):
    for j in range(h):
        if img.getpixel((i, j)) < 99:
            img.putpixel((i, j), (0))                           # 設為黑色
        else:
            img.putpixel((i, j), (255))                         # 設為白色
img.save("pic\\thresh2.jpg")                                    # 存檔
