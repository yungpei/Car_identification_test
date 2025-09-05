import cv2, glob
import numpy as np

files = glob.glob('digit\*.jpeg')    # 要合併的圖形
n = len(files)
spaceX = 10
spaceY = 8
offset = 1
img = cv2.imread(files[0])
h,w = img.shape[0], img.shape[1]

# 建立白色背景
bg = np.zeros((h+2*spaceY, (w+offset)*n+2*spaceX, 1), np.uint8)
bg.fill(255)

# 將數字加入白色背景中
for m, file in enumerate(files):
    gray = cv2.imread(file, 0)
    _,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    for row in range(h):
        for col in range(w):
            bg[spaceY+row][spaceX+col+(w+offset)*m] = thresh[row][col]  # 擷取圖形

    cv2.imwrite('merge.jpg', bg)    # 存檔

merge = cv2.imread("merge.jpg")
cv2.imshow("merge", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()