import numpy as np
import cv2

img_RGB = cv2.imread('chess.jpg', cv2.IMREAD_COLOR)

img_YCrCb = cv2.cvtColor(img_RGB,cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(img_YCrCb)

img_canny = cv2.Canny(y,100,200)
cv2.imshow('Canny_img',img_canny)



lines = cv2.HoughLinesP(img_canny,1,np.pi/180,150)   #img_canny에서 line 성분들의 시작점과 종점의 정보를 배열로 받아오는 명령문
for line in lines:      #lines 배열에서 하나의 line씩 가져오는 반복문
    x0, y0, x1, y1 = line[0]
    cv2.line(img_RGB,(x0,y0),(x1,y1),(0,0,255),2)



cv2.imshow('OG_img',img_RGB)

cv2.waitKey(0)