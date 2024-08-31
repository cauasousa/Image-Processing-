import numpy as np
import cv2
from matplotlib import pyplot as plt

# PASSA ALTA ->> ▪Preserva bordas e ruídos


img = cv2.imread('img//palhaco.png', cv2.IMREAD_GRAYSCALE)

assert img is  not  None , "o arquivo não pôde ser lido, verifique com os.path.exists()"

f = np.fft.fft2(img) #transformada de Fourier
fshift = np.fft.fftshift(f)
magnitude_espectro = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = rows//2, cols//2

mask = np.ones_like(img)

mask = 255 - mask
radius = 10
cv2.circle(mask, (crow, ccol), radius, (0,0,0), -1)


# aux = 5
# for i in range(rows):
#     for j in range(cols):

#         if ((crow-(15+aux) < i < crow+15+aux and ccol-(15+aux) < j < ccol+(15+aux))):
#             pass
#         elif (( crow - 45 < i < crow+30 and ccol - 45 < j < ccol+48 )):
        
#             fshift[i, j] = 0


# i = 0
# fshift[crow-30:crow+31, ccol-30:ccol+31] = 0

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
