import cv2

# cv2.Sobel é usado para DETECTAR bordas na imagem usando o operador Sobel. Duas versões são calculadas separadamente para as direções x e y.

image = cv2.imread('img//image-teste.jpg', cv2.IMREAD_GRAYSCALE)  # Carregar em escala de cinza para as operações de detecção de bordas

# cv2.Sobel(img, depth, dx, dy): Aplica o operador Sobel à imagem para detecção de bordas.
# img: A imagem de entrada.
# depth: A profundidade da imagem de saída.
# dx: A ordem da derivada em direção x.
# dy: A ordem da derivada em direção y.


# Aplicar Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)  # Derivada em x
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)  # Derivada em y


cv2.imshow('Original', image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)


cv2.waitKey(0)
cv2.destroyAllWindows()
