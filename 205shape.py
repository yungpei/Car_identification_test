import cv2

img = cv2.imread('pic\\person.jpg')
print("img.shape=", img.shape)
cv2.imshow("win1", img)

# 擷取圖片中的人臉
x,y,w,h = 240, 75, 140, 140
face = img[y: y + h, x: x + w]

# 顯示人臉中各點的像素值
x,y,w,h = 240, 75, 140, 140
for row in range(y, y+y):
    for col in range(x, x+w):
        print(img[row, col], end=" ")
    print()
print()

for row in range(y, y+h):
    for col in range(x, x+w):
        # 改變人臉的 B、G 值，R 值不變
        img[row, col][0] = 0   # 設定 B 值為 0
        img[row, col][1] = 50  # 設定 G 值為 50

cv2.imshow("win2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()