# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#peguei uma imagem com fundo branco e o J preto, 
# e converti para o fundo preto e J branco (ta parecido com o exemplo)
img = cv2.imread('img/j.jpg',0)
img = cv2.resize(img, (600, 500), interpolation = cv2.INTER_AREA)
img = cv2.bitwise_not(img)

j_com_ponto = cv2.imread('img/j_com_ponto.jpg',0)
j_com_ponto = cv2.resize(j_com_ponto, (600, 500), interpolation = cv2.INTER_AREA)
j_com_ponto = cv2.bitwise_not(j_com_ponto)


j_borrado = cv2.imread('img/j_borrado.jpg',0)
j_borrado = cv2.resize(j_borrado, (600, 500), interpolation = cv2.INTER_AREA)
j_borrado = cv2.bitwise_not(j_borrado)

kernel = np.ones((15,15),np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1) # substituindo o valor pelo de maior valor dentro do kernel
erosion = cv2.erode(img,kernel,iterations = 1) # substituindo o valor do pelo de menor valor dentro do kernel
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # Diferença entre Dilation e Erosion, gerando uma buraco dentro do J
# opening = cv2.dilate(erosion,kernel,iterations = 1) # Erosion seguida de Dilation, ocorre uma limpeza de ruido fora do J
opening = cv2.morphologyEx(j_com_ponto, cv2.MORPH_OPEN, kernel) # Erosion seguida de Dilation, Ocorre uma limpeza de ruido fora do J branco
closing = cv2.morphologyEx(j_borrado, cv2.MORPH_CLOSE, kernel) # Dilation seguida de Erosion, ocorre uma limpeza de ruido dentro do J branco


plt.subplot(341), plt.imshow(img)
plt.title('Imagem')
plt.subplot(342), plt.imshow(dilation)
plt.title('Dilation')
plt.subplot(343), plt.imshow(erosion)
plt.title('Erosion')
plt.subplot(344), plt.imshow(grad)
plt.title('Gradient')

plt.subplot(345), plt.imshow(j_com_ponto)
plt.title('Imagem com ponto')
plt.subplot(346), plt.imshow(opening)
plt.title('Opening')

plt.subplot(349), plt.imshow(j_borrado)
plt.title('J borrado')
plt.subplot(3,4,10), plt.imshow(closing)
plt.title('Closing')

plt.tight_layout()
plt.show()

