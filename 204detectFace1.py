import cv2

# 建立偵測物件
casc_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)

# 讀取要偵測的圖片
image = cv2.imread("pic\\people2.jpg")

# 進行偵測，辨識結果存於 faces 變數中
faces = faceCascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

imgheight = image.shape[0]  # 圖片高度
imgwidth = image.shape[1]   # 圖片寬度

cv2.rectangle(image, (10, imgheight-20), (110, imgheight), (0,0,0), -1) # 左下角黑色矩陣
cv2.putText(image, "Find " + str(len(faces)) + " face!", (10, imgheight-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

count = 1

# 迴圈逐一在臉部位置畫矩形以標示出臉部位置
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (128, 255, 0), 2)  # 框選臉部
    filename = "detect\\face" + str(count)+ ".jpg" # 存檔名稱
    image1 = image[y : y + h, x: x + w]         # 取得臉部圖形
    image2 = cv2.resize(image1, (400, 400))     # 重置圖形大小
    cv2.imwrite(filename, image2)
    count += 1

cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)             # 顯示
cv2.waitKey(0)                              # 使用者按任意鍵才執行第14段程式碼
cv2.destroyAllWindows("facedetect")         # 關閉所有視窗