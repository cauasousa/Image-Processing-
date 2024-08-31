import cv2

# cv2.GaussianBlur é aplicado para suavizar a imagem usando um filtro Gaussiano.


image = cv2.imread('img//image-teste.jpg', cv2.IMREAD_GRAYSCALE)  # Carregar em escala de cinza para as operações de detecção de bordas

# cv2.GaussianBlur(img, ksize, sigma): Aplica um filtro Gaussiano de borramento à imagem.
# img: A imagem de entrada.
# ksize: O tamanho do kernel de borramento. Deve ser um número ímpar positivo.
# sigma: O desvio padrão do kernel Gaussiano


# Aplicar filtro Gaussiano
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)


# Exibir as imagens resultantes
cv2.imshow('Original', image)
cv2.imshow('Gaussian Blur', blurred_image)



cv2.waitKey(0)
cv2.destroyAllWindows()