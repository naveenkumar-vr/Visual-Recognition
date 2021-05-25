import cv2
import numpy as np
# minRange for min skin color Rnage
# maxRange for maximum skin color Range
minRange = np.array([0,133,77],np.uint8)
maxRange = np.array([235,173,127],np.uint8)
image = cv2.imread("Assignment1_Rishabh_Pant.jpg")
# change our image bgr to ycr using cvtcolor() method 
YCRimage = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
cv2.imwrite("con.jpg",YCRimage)
# apply min or max range on skin area in our image
skinArea = cv2.inRange(YCRimage,minRange,maxRange)
# detecting skin area
detectedSkin = cv2.bitwise_and(image, image, mask = skinArea)
cv2.imwrite("output.png", np.hstack([image,detectedSkin]))
