import cv2
import matplotlib.pyplot as plt

img = cv2.imread("assets/img/studentCard.jpg")
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite("hog_result.png", img2)


