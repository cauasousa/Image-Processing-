# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/u.png',0)
img = cv2.resize(img, (600, 500), interpolation = cv2.INTER_AREA)

# 500/600 = 250/300 = 50/70 = 25/35 = 10/14 

### OPERACAO 1
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15,15))
kernel[:,8:] = 0
kernel[8:,:] = 0

erosion = cv2.erode(img,kernel,iterations = 8) 

### OPERACAO DO FUNDO
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) 

### JUNCAO OP1 + FUNDO
resolucao1 = cv2.bitwise_or(grad, erosion)

### OPERACAO 2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19,29))
erosion = cv2.erode(img,kernel,iterations = 7)

kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (15,31))
erosion = cv2.dilate(erosion,kernel,iterations = 5) 

### JUNCAO OP2 + FUNDO
resolucao2 = cv2.bitwise_or(grad, erosion)

### OPERACAO 3
kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (15,25))
dilate = cv2.dilate(img,kernel,iterations = 5) 

kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (19,29)) # -> redondo
teste3 = cv2.erode(dilate,kernel,iterations = 2) 

### JUNCAO OP3 + FUNDO
resolucao3 = cv2.bitwise_xor( teste3, grad)

###########################################################################33

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(resolucao1)
plt.title('Resolucao 1')
plt.subplot(223), plt.imshow(resolucao2)
plt.title('Resolucao 2')
plt.subplot(224), plt.imshow(resolucao3)
plt.title('Resolucao 3')

plt.tight_layout()
plt.show()