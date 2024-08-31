import cv2
import numpy as np
import random
sal = 0.00000
img = cv2.imread("img//arara.jpeg", flags=cv2.IMREAD_GRAYSCALE)

def noise(image,prob):
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


def reducion(frame, width, height ):

    mediaColuna = int(width/3)
    mediaHeight = int(height/3)

    espace = np.zeros( (mediaHeight, mediaColuna), dtype=np.uint8)
    espaceMedia = np.zeros( (mediaHeight, mediaColuna), dtype=np.uint8)

    for linha in range(mediaHeight):
        for coluna in range(mediaColuna):
            
            espace[linha][coluna] = frame[(linha*3)+1][(coluna*3)+1]

            media = 0
            for z in range(3):
                for x in range(3):
                    media += frame[(linha*3)+z][(coluna*3)+x]

            media = media/9
            espaceMedia[linha][coluna] = media
    
    return espace, espaceMedia





if img is None:
    print('ERRO')
else:    

    frame, frame_media = reducion(frame=img, height=img.shape[0], width=img.shape[1])
    cv2.imshow("Img Original", img)
    cv2.imshow("vizinhança-8", frame)
    cv2.imshow("media vizinhança-8.", frame)


    while True:

        cv2.imshow("APERTE A or Z - SAL E PIMENTA ", noise(img, sal))
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        if cv2.waitKey(0) & 0xFF == ord('a'):
            
            if(sal < 1.000):
                sal += 0.005
        if cv2.waitKey(0) & 0xFF == ord('z') :
            
            if sal > 0.000:
                sal -= 0.005
    

    cv2.destroyAllWindows()
