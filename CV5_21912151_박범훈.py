import numpy as np
import cv2
import math


#RGB : openCV 에서는 BGR
#YCbCr : openCV에서 YCrCb

#원본이미지 받아오기
OG_RGB_img = cv2.imread('drogba.jpg')
#cv2.imshow('drogba.jpg',OG_RGB_img)

#YCbCr 이미지로 변환
YCrCb_img = cv2.cvtColor(OG_RGB_img,cv2.COLOR_BGR2YCrCb)
#cv2.imshow('YCnCr_img',YCrCb_img)

#y성문만 HE(HistogramEquilization) 시행
y_auto, cr, cb = cv2.split(YCrCb_img)
y_auto = cv2.equalizeHist(y_auto)

YCbCr_img_re_HE_auto = cv2.merge([y_auto,cr,cb])
#cv2.imshow('YCbCr_img_re_HE',YCbCr_img_re_HE_auto)
#Y성분만 HE한 이미지를 RGB 이미지로 전환
Re_RGB_img_auto = cv2.cvtColor(YCbCr_img_re_HE_auto,cv2.COLOR_YCrCb2BGR)
cv2.imshow('Re_RGB_img_auto',Re_RGB_img_auto)
#openCV를 이용해 HE후 복원한 이미지의 PSNR 구하기
PSNR_auto= cv2.PSNR(OG_RGB_img,Re_RGB_img_auto)




###########################################################################
##내가 수식으로 구하는 부분
y_my, cr, cb = cv2.split(YCrCb_img)

height, width, channels = YCrCb_img.shape
total_pixel = height * width
hist, bins = np.histogram(y_my, 256, [0, 256])#y 성분만 HE 해야되는데 전체 이미지를 히스토그램화 시켜가지고 문제가있었음
#np.histogram(xxx, num , [a, b]) : xxx를 x축 값은 num+1개 있고 범위는 a~b이다
#a~b를 num+1개의 항목으로 나타내라 -> 0~255를 255+1개의 항목으로 나타내라
#hist : xxx자리의 이미지파일의 모든 픽셀이 각 0~255에 해당하는 갯수를 표현한것 ex) [1 2 2 3 3 3] -> [0 1 2 3] (0~3)
#bins : x축의 각 값을 표현한 부분(각 부분의 갯수 표현아님)


sum = hist.cumsum()              #누적 빈도수 구하는 부분

max_value = 0
for i in range(255):
    if(max_value < hist[i]):
        max_value = hist[i]     # 최대 픽셀 value 구하는 부분
table = np.zeros(256)           # histogame Equalization table 만들기위해 0으로 초기화된 배열 생성

for i in range(255):
    table[i] = round(256 * sum[i] / total_pixel)# HE table의 값 넣어주는 부분                    

for i in range(height):
    for j in range(width):
        y_my[i][j] = table[y_my[i][j]]          # 이미지의 각 y 성분의 값에 해당하는 HE table의 값 넣어주는 부분

YCbCr_img_re_HE_my = cv2.merge([y_my,cr,cb])    # 바꿔준 y성분으로 다시 YCbCr 이미지 생성
Re_RGB_img_my = cv2.cvtColor(YCbCr_img_re_HE_my,cv2.COLOR_YCrCb2BGR)    # 수동으로 HE한 YCbCr 이미지를 RGB 이미지로 변환
cv2.imshow('Re_RGB_img_my',Re_RGB_img_my)
PSNR_my = cv2.PSNR(OG_RGB_img,Re_RGB_img_my)

print('openCV 함수를 이용한 PSNR : ',PSNR_auto)
print('직접 계산하여 변환한 PSNR : ',PSNR_my)
cv2.waitKey()


