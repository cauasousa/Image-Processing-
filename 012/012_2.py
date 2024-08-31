# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Tophat e Blackhat: revela REGIÕES de maior brilho

img = cv2.imread('img/veiculo.png',0)
img = cv2.resize(img, (600, 500), interpolation = cv2.INTER_AREA)

kernel = np.ones(shape=(15,15), dtype=np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=1)  
blackhat = cv2.morphologyEx(tophat, cv2.MORPH_BLACKHAT, kernel, iterations=1)

###########################################################################33

plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Imagem')
plt.subplot(222), plt.imshow(tophat, cmap='gray')
plt.title('Tophat')
plt.subplot(223), plt.imshow(blackhat, cmap='gray')
plt.title('Tophat + Blackhat')

plt.tight_layout()
plt.show()