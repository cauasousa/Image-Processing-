import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
 
img1 = cv.imread('img/imageBatata.png',cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('img\\imageFull.png',cv.IMREAD_GRAYSCALE) # trainImage


# Initiate ORB detector
orb = cv.ORB_create( 
    nfeatures = 10000, 
    scaleFactor = 1.79999999999, 
    # firstLevel = 0,
    # nlevels = 10,
    # edgeThreshold = 3,
    # WTA_K = 4,
    # scoreType = cv.ORB_FAST_SCORE ,
    # patchSize = 20,
    # fastThreshold = 25,
)
 
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
 
# Match descriptors.
matches = bf.match(des1,des2)
 
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# pega os melhores
matches=matches[:70]
# matches=matches[:0]

# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches,None,flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
 
plt.imshow(img3),plt.show()