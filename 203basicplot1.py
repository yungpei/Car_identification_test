import cv2
import numpy as np

cv2.namedWindow("plot")  # 建立視窗

# 建立一張 512x512 黑色背景 (3 通道 BGR)
image = np.zeros((512, 512, 3), np.uint8)

# 畫線、矩形、圓形
cv2.line(image, (50, 50), (500, 200), (255, 0, 0), 2)           # 藍色直線
cv2.rectangle(image, (100, 200), (180, 300), (0, 255, 0), 3)    # 綠色空心矩形
cv2.rectangle(image, (300, 200), (350, 260), (0, 0, 255), -1)   # 紅色實心矩形
cv2.circle(image, (450, 300), 40, (255, 255, 0), -1)            # 實心圓

# 多邊形
pts = np.array([[300, 300], [300, 340], [350, 320]], np.int32)
pts = pts.reshape((-1, 1, 2))  # OpenCV 要求格式
cv2.polylines(image, [pts], True, (0, 255, 255), 2)             # 黃色多邊形

# 加上文字
cv2.putText(image, "No bg.jpg", (20, 420), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)

# 顯示結果
cv2.imshow("plot", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
