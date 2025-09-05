import cv2
import numpy as np

# 建立桃紅色畫布
canvas = np.ones((200, 250, 3), dtype="uint8")
print(canvas.shape)
canvas[:] = (125, 40, 255)
cv2.imshow('canvas', canvas)

bg = np.zeros((200, 250, 1), np.uint8)
print(bg.shape)
bg.fill(255)

for j in range(200):
    for i in range(250):
        bg[j][i].fill(255-i)

cv2.imshow("bg", bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
