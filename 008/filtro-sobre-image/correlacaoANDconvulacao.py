import cv2
import numpy as np

# cv2.filter2D: Aplica um filtro customizado à imagem.


image = cv2.imread('img//image-teste.jpg')
image = cv2.imread('img//image-teste.jpg', cv2.IMREAD_GRAYSCALE)


def correlation(image, kernel):
    result = cv2.filter2D(image, -1, kernel)
    # -1 mantem a profundidade
    return result


              #Matriz exemplos 

# Definir um kernel de nitidez
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# Definir um kernel de borramento
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16

#detectar bordas - kernel_laplacian
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)
                   
#Realce de Características - kernel_line
kernel = np.array([[-1, -1, -1],
                        [2, 2, 2],
                        [-1, -1, -1]], dtype=np.float32)


result = correlation(image, kernel)

cv2.imshow('Original', image)
cv2.imshow('Correlacao', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
