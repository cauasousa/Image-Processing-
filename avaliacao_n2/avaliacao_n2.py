import cv2 
import numpy as np 

# Let's load a simple image with 3 black squares 
image = cv2.imread('C:/Users/CauaS/programacao/Python-Development/worksImage/ImageProcesss/avaliacao_n2/Original.png') 
img = cv2.resize(image, (300, 300), interpolation = cv2.INTER_AREA)
img_copia = cv2.resize(image, (300, 300), interpolation = cv2.INTER_AREA)


imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 100, 255, 0)



def drawCir():
    
    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT_ALT, 1.5, 20, param1=50, param2=0.99, minRadius=0,maxRadius=0)
    # circles = cv2.HoughCircles(imgray,cv2.HOUGH_GRADIENT,1,20,
    #                         param1=50,param2=30,minRadius=0,maxRadius=0)

    # print(circles)
    
    circles = np.uint16(np.around(circles))
    

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0, 0, 255),-1)
        # draw the center of the circle
        # cv2.circle(img,(i[0],i[1]),2,(0,0,255),-1)



contours, x = cv2.findContours(thresh, 1, 2) 
for i in contours:

    cnt = i
    M = cv2.moments(cnt)

    epsilon = 0.001*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    (x, y), radius = cv2.minEnclosingCircle(cnt)
    cor = (0, 255, 0)
    if radius < 31:
        continue
    
    cv2.drawContours(img, [approx], -1, cor, -1) 

drawCir()  

# cv2.imshow('detected circles',cimg)
cv2.imshow('Resultado', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 