import numpy as np
import cv2


### 자동 전환
# 원본 이미지 출력
OG_img_auto = cv2.imread('drogba.jpg', cv2.IMREAD_COLOR)
cv2.imshow('OG_img',OG_img_auto)                                     ## 이까지만하면 Report 1

# YCbCr 이미지 출력
YCbCr_img_auto = cv2.cvtColor(OG_img_auto,cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCnCr_img',YCbCr_img_auto)
# RGB 이미지 복원
RGB_re_img_auto = cv2.cvtColor(YCbCr_img_auto,cv2.COLOR_YCrCb2BGR)
cv2.imshow('RGB_img',RGB_re_img_auto)

cv2.waitKey()