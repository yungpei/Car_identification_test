import cv2
import numpy as np
from PIL import Image

img = Image.open('pic\\example.png')        # Pillow 預設格式是 RGB
img.show()

# Pillow to OpenCV
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV", img)

cv2.waitKey(0)
cv2.destroyAllWindows()