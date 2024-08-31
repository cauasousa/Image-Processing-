import cv2 
import numpy as np 

# Let's load a simple image with 3 black squares 
image = cv2.imread('img/moedas.png') 
img = cv2.resize(image, (500, 360), interpolation = cv2.INTER_AREA)

# Grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

rows = gray.shape[0]

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 3,
param1=30, param2=30,
minRadius=60, maxRadius=88)


if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:

        center = (i[0], i[1])
        # circle center

        cv2.circle(gray, center, 1, (0, 0, 0), 3)
        # circle outline
        radius = i[2]

        cv2.circle(gray, center, radius, (0, 0, 0), 3)


cv2.imshow('Contours', gray) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
