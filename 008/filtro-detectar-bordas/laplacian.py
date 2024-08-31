import cv2

# cv2.Laplacian é aplicado para DETECTAR bordas na imagem usando o operador Laplaciano.


image = cv2.imread('img//image-teste.jpg', cv2.IMREAD_GRAYSCALE)  # Carregar em escala de cinza para as operações de detecção de bordas

# cv2.Laplacian(img, depth): Aplica um filtro Laplaciano à imagem.
# img: A imagem de entrada.
# depth: A profundidade da imagem de saída.

# Aplicar Laplacian
laplacian_image = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow('Original', image)

cv2.imshow('Laplacian', laplacian_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
