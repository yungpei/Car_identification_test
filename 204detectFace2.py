import cv2

# 建立偵測物件
casc_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)

# 讀取要偵測的圖片
image = cv2.imread("pic\\people2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 偵測人臉（調整參數）
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,       # 提高 minNeighbors 可以減少誤檢
    minSize=(50, 50),     # 限制最小臉的大小
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("偵測到 {} 張臉".format(len(faces)))

count = 1

# 畫框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (128, 255, 0), 2)
    filename = "detect\\face" + str(count)+ ".jpg" # 存檔名稱
    image1 = image[y : y + h, x: x + w]         # 取得臉部圖形
    image2 = cv2.resize(image1, (400, 400))     # 重置圖形大小
    cv2.imwrite(filename, image2)
    count += 1

cv2.imshow("facedetect", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
