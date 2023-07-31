import numpy as np
import cv2

OG_img_RGB = cv2.imread('drogba.jpg', cv2.IMREAD_COLOR)
cv2.imshow('OG_img',OG_img_RGB)

OG_YCrCb_img = cv2.cvtColor(OG_img_RGB,cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(OG_YCrCb_img)

for i in range(5):
    y = cv2.GaussianBlur(y,(3,3),1)

Re_img_YCrCb = cv2.merge([y,cr,cb])
Re_img_RGB = cv2.cvtColor(Re_img_YCrCb,cv2.COLOR_YCrCb2BGR)

cv2.imshow('Re_img',Re_img_RGB)

cv2.waitKey(0)