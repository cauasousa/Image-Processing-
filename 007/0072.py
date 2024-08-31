# coding=utf-8
import cv2
import numpy as np

img2Logo = cv2.imread("img//opencv-logo-small.png")

def renderizando_logo(img1, imgLogo):
    imgLogo = cv2.resize(imgLogo, (80, 80),  interpolation=cv2.INTER_AREA)
    
    res=np.zeros(img1.shape, np.uint8)
    res = cv2.bitwise_not(res) 
    
    for linha in range(imgLogo.shape[0]):
        for coluna in range(imgLogo.shape[1]):
            if imgLogo[linha, coluna][0] > 5 and imgLogo[linha, coluna][1] > 5 and imgLogo[linha, coluna][2] > 5:
                res[10 + linha, 10 + coluna] = imgLogo[linha, coluna]

    return res


def logo_frame(img1):
    return cv2.bitwise_and(img1, renderizando_logo(img1, img2Logo))

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro ao acessar camera ou abrir o vídeo")
else:

    while capture.isOpened():

        ret, frame = capture.read()
        
        if ret is True:

            frame = logo_frame(frame)
            cv2.imshow('Input', frame)
            
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()