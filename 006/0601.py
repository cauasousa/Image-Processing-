# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('img//color_red.jpg')
res = img.copy()
rows,cols = img.shape[:2]
x_angle, y_angle, angle = -1, -1, 0

def draw_circle(event,x,y,flags,param):

    global x_angle, y_angle, res, angle

    if event == cv2.EVENT_LBUTTONUP:
        
        x_angle = x
        y_angle = y
        angle = 0.5
        cv2.circle(res,(x_angle,y_angle),4, (255, 255, 255),-1)

    else:

        cv2.circle(res,(x_angle,y_angle),4, (255, 255, 255),-1)



def transform():

    global x_angle, y_angle, res, angle

    M = cv2.getRotationMatrix2D((x_angle,y_angle), angle,1)  #é possível rotacionar aqui
    
    res = cv2.warpAffine(res, M, (cols,rows))
    

cv2.imshow('res',res)

while 1:

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if cv2.waitKey(30) & 0xFF == ord('r'):
        angle = 2
        transform()
        
    else:
        angle = 0
        
    cv2.namedWindow('res')
    cv2.setMouseCallback('res', draw_circle)
    cv2.imshow('res',res)
    
cv2.waitKey(0)
cv2.destroyAllWindows()