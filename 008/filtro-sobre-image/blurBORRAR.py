import cv2

image = cv2.imread('img//image-teste.jpg')

# Aplicar o filtro de borramento
blurred_image = cv2.blur(image, (5, 5))  # O segundo argumento é o tamanho do kernel de borramento


cv2.imshow('Original', image)
cv2.imshow('Blur', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
