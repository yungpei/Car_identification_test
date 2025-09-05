import cv2
from PIL import Image

img = cv2.imread('pic\\example.png')        # OpenCV 預設格式 BGR
cv2.imshow("OpenCV", img)

# OpenCV to Pillow
image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
image.show()

cv2.waitKey(0)
cv2.destroyAllWindows()