import cv2 
import numpy as np 

# Let's load a simple image with 3 black squares 
image = cv2.imread('C:/Users/CauaS/programacao/Python-Development/worksImage/ImageProcesss/avaliacao_n2/Original.png') 
img = cv2.resize(image, (300, 300), interpolation = cv2.INTER_AREA)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 100, 255, 0)

# jeito de realizar 2
# resultado = cv2.drawContours(img, contornos, -1, (0,255,0), -1)   
# resultado = cv2.drawContours(resultado, contornos, 9, (0,0,255), -1)   

contours, x = cv2.findContours(thresh, 1, 2) 

for i in contours:

    cnt = i
    M = cv2.moments(cnt)

    epsilon = 0.00001*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    (x, y), radius = cv2.minEnclosingCircle(cnt)
    cor = (0, 255, 0)

    if radius < 31: 
        cor = (0, 0, 255)
    
    cv2.drawContours(img, [approx], -1, cor, -1)   

cv2.imshow('Resultado', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
