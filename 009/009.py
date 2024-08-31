import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img//palhaco.png', cv2.IMREAD_GRAYSCALE)

######################### PARTE IMPORTANTE ##################################################

f = np.fft.fft2(img) #transformada de Fourier
fshift = np.fft.fftshift(f)
magnitude_espectro = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = rows//2, cols//2

mask = np.zeros((rows, cols), np.uint8)

radius = 23
cv2.circle(mask, (crow, ccol), radius, (255,255,255), -1)

dft_shift_masked = np.multiply(fshift, mask) #

back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
img_filtered = np.fft.ifft2(back_ishift_masked)
img_back = np.abs(img_filtered)

##############################################################################################3
plt.subplot(2, 2, 1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2),plt.imshow(magnitude_espectro, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

# plt.scatter(crow, ccol, color='red', s=5, marker='o')

plt.subplot(2, 2, 3),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()