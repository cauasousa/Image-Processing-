# coding=utf-8
import cv2
import numpy as np


img1 = cv2.imread("img//ifma-caxias.jpg")

img2Logo = cv2.imread("img//logo-if-vertical.png")

def renderizando_logo(imgLogo):
    imgLogo = cv2.resize(imgLogo, (80, 100),  interpolation=cv2.INTER_AREA)
    
    res=np.zeros(img1.shape, np.uint8)
    res = cv2.bitwise_not(res) 
    
    for linha in range(imgLogo.shape[0]):
        for coluna in range(imgLogo.shape[1]):

            if imgLogo[linha, coluna][0] < 255 and imgLogo[linha, coluna][1] < 255 and imgLogo[linha, coluna][2] < 255:
                res[10 + linha, 10 + coluna] = imgLogo[linha, coluna] 
    

    return res


logo_background = renderizando_logo(img2Logo)

bit_and = cv2.bitwise_and(img1, logo_background)

cv2.imshow("imgand", bit_and) 

cv2.waitKey(0)
cv2.destroyAllWindows()