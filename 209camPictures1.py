import cv2
cv2.namedWindow("frame")

cap = cv2.VideoCapture(0)
while(cap.isOpoened()):
    ret, img = cap.read()
    if ret == True:
        cv2.imshow("frame", img)
        k = cv2.waitKey(100)
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("pic\\catch.jpg", img)
            break
cap.release()
cv2.destroyWindow("frame")

### 因為沒有鏡頭 ###