import cv2

cv2.namedWindow("ShoowImage")               # 建立視窗

image = cv2.imread("pic\\example.png", 0)   # 灰階模式讀取

cv2.imshow("ShowImage", image)              # 顯示

cv2.imwrite("pic\\examplecopy1.png", image)
cv2.imwrite("pic\\examplecopy2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
                                            # 以品質 50 儲存檔案

cv2.waitKey(0)                              # 使用者按任意鍵才執行第14段程式碼
cv2.destroyAllWindows("ShowImage")                     # 關閉所有視窗