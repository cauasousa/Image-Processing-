import cv2

# reduzir o ruído "sal e pimenta"
# cv2.medianBlur é usado para aplicar um filtro de mediana para suavizar a imagem.

image = cv2.imread('img//image-teste.jpg', cv2.IMREAD_GRAYSCALE)  # Carregar em escala de cinza para as operações de detecção de bordas
image = cv2.imread('img//image-teste.jpg')  # Carregar em escala de cinza para as operações de detecção de bordas

# cv2.medianBlur(img, ksize): Aplica um filtro de mediana de borramento à imagem.
# img: A imagem de entrada.
# ksize: O tamanho do kernel de borramento. Deve ser um número ímpar positivo.

# Aplicar filtro de mediana
median_blurred_image = cv2.medianBlur(image, 7)


cv2.imshow('Original', image)

cv2.imshow('Median Blur', median_blurred_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
