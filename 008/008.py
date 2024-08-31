import cv2
import numpy as np
import random

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

def sal_pimenta(image, prob):

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]

    return output

def draw_frame():

    global RED
    
    output = np.zeros((500, 500, 3), np.uint8)
    
    for i in range(500):
        for j in range(500):
            output[i, j] = (255, 255, 255)

    print(output[1, 1])

    cv2.circle(output, (150, 250), 30, (0, 0, 255), -1)
    cv2.circle(output, (350, 250), 80, (0, 0, 255), -1)
    cv2.circle(output, (150, 50), 30, RED, -1)
    cv2.circle(output, (50, 50), 30, RED, -1)
    cv2.circle(output, (400, 50), 30, BLACK, -1)
    
    return output

image = sal_pimenta(draw_frame(), 0.09)
resultado = cv2.medianBlur(image, 5)


cv2.imshow('Original', image)

cv2.imshow('Resultado', resultado)


cv2.waitKey(0)
cv2.destroyAllWindows()