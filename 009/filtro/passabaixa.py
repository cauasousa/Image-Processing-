import numpy as np
import cv2
from matplotlib import pyplot as plt

# PASSA BAIXO ->> ▪Suaviza e reduz ruído


img = cv2.imread('img//palhaco.png', cv2.IMREAD_GRAYSCALE)

assert img is  not  None , "o arquivo não pôde ser lido, verifique com os.path.exists()"

f = np.fft.fft2(img) #transformada de Fourier
fshift = np.fft.fftshift(f)
magnitude_espectro = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = rows//2, cols//2


# i = 5
# crow = crow 
# ccol = 0 + 80

# print(crow, ccol)
# fshift[(crow - i):(crow + i), (ccol-i):(ccol + i)] = 0

mask = np.ones_like(img)

# mask = 255 - mask
radius = 23
cv2.circle(mask, (crow, ccol), radius, (255,255,255), -1)



dft_shift_masked = np.multiply(fshift, mask) 

back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
img_filtered = np.fft.ifft2(back_ishift_masked)
img_back = np.abs(img_filtered)


# f_ishift = np.fft.ifftshift(fshift)
# img_back = np.fft.ifft2(f_ishift)
# img_back = np.real(img_back)



plt.subplot(2, 2, 1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2),plt.imshow(magnitude_espectro, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

# Marcar um ponto específico no espectro de frequência
# plt.scatter(crow-31, ccol-31, color='red', s=5, marker='o')
# plt.scatter(crow+36, ccol-24, color='red', s=5, marker='o')
plt.scatter(crow, ccol, color='red', s=5, marker='o')


plt.subplot(2, 2, 3),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
 


plt.show()
