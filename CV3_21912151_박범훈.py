import numpy as np
import cv2
import math

#원본이미지 받아오기
OG_RGB_img_my = cv2.imread('drogba.jpg')
height, width, channel = OG_RGB_img_my.shape
B = OG_RGB_img_my[...,0]
G = OG_RGB_img_my[...,1]
R = OG_RGB_img_my[...,2]
cv2.imshow('drogba.jpg',OG_RGB_img_my)


#YCbCr 이미지 생성
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

### RGB 사진 수식을 통한 복원
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

##OpenCV 함수를 이용해서 PSNR 구하기
PSNR_cv2 = cv2.PSNR(OG_RGB_img_my,RGB_img_my)
print("cv2를 사용한 PSNR : {}".format(PSNR_cv2))


##직접 수식으로 구한 PSNR 구하기
R_mse = np.mean((R-R_re_my)**2)
G_mse = np.mean((G-G_re_my)**2)
B_mse = np.mean((B-B_re_my)**2)
total_mse = R_mse + G_mse + B_mse

PSNR_my = 10 * math.log10((255**2)/total_mse)
print("직접 계산한 PSNR : {}".format(PSNR_my))


##PSNR_my




cv2.waitKey(0)
cv2.destroyAllWindows()