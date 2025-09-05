import cv2

cv2.namedWindow("ShoowImage1")
cv2.namedWindow("ShoowImage2")
# 建立兩個視窗

image1 = cv2.imread("pic\\example.png")      # 彩色模式讀取
image2 = cv2.imread("pic\\example.png", 0)   # 灰階模式讀取

cv2.imshow("ShowImage1", image1)             # 顯示
cv2.imshow("ShowImage2", image2)

cv2.waitKey(0)                               # 使用者按任意鍵才執行第14段程式碼
cv2.destroyAllWindows()                      # 關閉所有視窗