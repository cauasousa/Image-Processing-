# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('img//color_red.jpg')

trys = False

def ajuste(img,br,ctr):
    print(br, ctr)

    brilho=[br,br,br]
    contraste=[ctr,ctr,ctr]
    img_copia = img.copy()

    res=np.zeros(img.shape, np.uint8)
    
    width, heigth, _ = img.shape

    for y in range(0, width):
        for x in range(0, heigth):
            res[y, x] = np.minimum(np.minimum((img_copia[y,x]*contraste), [255, 255, 255]) + brilho , [255,255,255])

    return res

def negativo(img):

    global trys
    img_copia = img.copy()

    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            img[x, y] = img_copia[x, y] if not trys else 255 - img[x, y]

    return img


cv2.namedWindow('Brilho')

brilho = 0
constraste=1
result=imagem
img_copy = imagem.copy()
x = 0

while(True):
    brilho=min(max(brilho, 0 ), 255)
    constraste=min(max(constraste, 0.01 ), 255)
    result=ajuste(imagem,brilho, constraste)

    cv2.imshow('Brilho',negativo(result))

    
    k=cv2.waitKey(0)
    
    if k == ord('q'):
        break
    elif k == ord('a'):
        brilho += 50
        
    elif k == ord('z'):
        brilho -= 50

    elif k == ord('s'):
        constraste += 1.1
        
    elif k == ord('x'):
        constraste -= 0.1

    elif k == ord('n'):
        trys = not trys
        

cv2.destroyAllWindows()
