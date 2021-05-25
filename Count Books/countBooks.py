import cv2
import numpy as np

img = cv2.imread("Bookshelf.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
gray = cv2.GaussianBlur(gray, (3,3), 0)
cv2.imshow("gray", gray)

canny = cv2.Canny(gray, 100, 500)
cv2.imshow("edged", canny)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 5))
dilated = cv2.dilate(canny, kernel, iterations=1)
dilated = cv2.Canny(dilated, 0, 0)

final = img.copy()
count=0
contours,hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for i, cnt in enumerate(contours):
    x,y,w,h = cv2.boundingRect(cnt)
    count+=1
    rect = cv2.minAreaRect(cnt)
    box = np.int0(cv2.boxPoints(rect))
    cv2.rectangle(final,(x,y),(x+w,y+h),(0,255,0),2)
print("Number of books: ")
print(count)

cv2.waitKey(0)
