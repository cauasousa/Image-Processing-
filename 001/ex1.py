import cv2
import math
import numpy as np

imgm = cv2.imread("img//color_red.jpg")

if imgm is None:
    print('ERRO')
    

img = cv2.resize(imgm, (250, 350))
imgCinza = img.copy()
imgCopia = img.copy()
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
red = img_hsv.copy()

def conv(wigth, height, img):

    for i in range(height):

        for j in range(wigth):
        
            h, s, v = img[i, j]
            verificar_S = ((1 + (h / 20)) * 100)
            verifica_V = (1 + (h / 20)) * 1
            verificar_S179 = ( (1 + ((( 179 - h )) / 10) ) * 40 )
            verifica_V179 = ( (1 + (( 179 - h ) / 10) ) * 40 )

            if (((0 <= h and h <= 20) and s > verificar_S and v > verifica_V)) or ((168 <= h <= 179 and s > verificar_S179 and v > verifica_V179)):

                continue
            
            else:

                global imgCinza, imgCopia
                value = sum(imgCopia[i, j]) * 0.33
                imgCinza[i, j] = [value, value, value]
                img[i, j] = [0, 0, 255]

height, wigth, camada = img_hsv.shape


conv(wigth, height, red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

cv2.imshow("Img", img)
cv2.imshow("Img HSV", img_hsv)
cv2.imshow("Img RED", red)
cv2.imshow("Img Cinza", imgCinza)

cv2.waitKey(0)
cv2.destroyAllWindows()
