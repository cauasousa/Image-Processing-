# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('img//color_red.jpg')

rows,cols = img.shape[:2]

# M = np.float32([[1,0,100],[0,1,50]]) # Aqui é possível fazer a translação
# M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1) #é possível rotacionar aqui

# pts1 = [[50,50],[200,50],[50,200]]
# pts2 = [[10,100],[200,50],[100,250]]
# M = cv2.getAffineTransfqorm(np.float32(pts1),np.float32(pts2)) # fazendo a ascilhamento

# res = cv2.warpAffine(img,M,(cols,rows))
print(rows, cols)
pts1 = [[200,100],[400,100],[50,400],[550,400]]
pts2 = [[0,0],[300,0],[0,300],[300,300]]

M = cv2.getPerspectiveTransform(np.float32(pts1),np.float32(pts2))
# res = cv2.warpPerspective(img,M,(300,300))
res = cv2.warpPerspective(img,M,(cols,rows))

# cv2.circle(img,(200,100),3, (255, 255, 255),-1)
# cv2.circle(img,(400,100),3, (255, 255, 255),-1)
# cv2.circle(img,(50,400),3, (255, 255, 255),-1)
# cv2.circle(img,(550,400),3, (255, 255, 255),-1)
cv2.circle(img,(300,0),3, (255, 255, 255),-1)
cv2.circle(img,(0,300),3, (255, 255, 255),-1)
cv2.circle(img,(300,300),3, (255, 255, 255),-1)



# for pt in pts1:
#     cv2.circle(img,pt,5,(0,0,255),-1)

# for pt in pts2:
#     cv2.circle(res,pt,5,(0,0,255),-1)

cv2.imshow('img',img)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()