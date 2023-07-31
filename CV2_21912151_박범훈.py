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


### 수동 전환
# YCbCr 이미지 출력
OG_img_my = cv2.imread('drogba.jpg')
height, width, channel = OG_img_my.shape
B = OG_img_my[...,0]
G = OG_img_my[...,1]
R = OG_img_my[...,2]

y = np.zeros((height,width),dtype = float)
Cb = np.zeros((height,width),dtype = float)
Cr = np.zeros((height,width),dtype = float)

for i in range(height):
    for j in range(width):
        y[i][j] = 0.257 * R[i][j] + 0.504 * G[i][j] + 0.098 * B[i][j] + 16
        Cb[i][j] = -0.148 * R[i][j] - 0.291 * G[i][j] + 0.439 * B[i][j] + 128       # 7페이지가 아니라?
        Cr[i][j] = 0.439 * R[i][j] - 0.368 * G[i][j] - 0.071 * B[i][j] + 128        # 왜 컴퓨터비전 강의자료4 9p 공식 넣어야됨?

YCbCr_img_my = (np.dstack((y, Cr, Cb))).astype(np.uint8)
cv2.imshow('YCbCr_img_my',YCbCr_img_my)

### RGB 사진 복원
R_re_my = np.zeros((height,width),dtype = float)
G_re_my = np.zeros((height,width),dtype = float)
B_re_my = np.zeros((height,width),dtype = float)

for i in range(height):
    for j in range(width):
        R_re_my[i][j] = 1.164 * (y[i][j] - 16) + 1.596 * (Cr[i][j]-128)
        G_re_my[i][j] = 1.164 * (y[i][j] - 16) - 0.813 * (Cr[i][j]-128) - 0.391 * (Cb[i][j] - 128)
        B_re_my[i][j] = 1.164 * (y[i][j] - 16) + 2.018 * (Cb[i][j]-128)

RGB_img_my = (np.dstack((B_re_my, G_re_my, R_re_my))).astype(np.uint8)
cv2.imshow('RGB_img_my',RGB_img_my)

#PSNR_cv2 = cv2.PSNR(RGB)

cv2.waitKey(0)
cv2.destroyAllWindows()