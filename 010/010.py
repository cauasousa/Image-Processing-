import cv2
import numpy as np


img1 = cv2.imread("img//ifma-caxias.jpg")
img1 = cv2.resize(img1, (500, 400),  interpolation=cv2.INTER_AREA)

img2Logo = cv2.imread("img//logo.png")
img2Logo = cv2.resize(img2Logo, (500, 400),  interpolation=cv2.INTER_AREA)

rows, cols, _ = img1.shape

def renderizando_logo(imgLogo):
    imgLogo = cv2.resize(imgLogo, (int(rows*0.2), int(cols*0.1)),  interpolation=cv2.INTER_AREA)
    
    res=np.zeros(img1.shape, np.uint8)
    res = cv2.bitwise_not(res) 
    
    for linha in range(imgLogo.shape[0]):
        for coluna in range(imgLogo.shape[1]):
            g, b, r = imgLogo[linha, coluna]
            if (b, g, r) < (255, 255, 255) and (b, g, r) > (0, 0, 0):
                res[10 + linha, 10 + coluna] = imgLogo[linha, coluna]
    

    return res

def img_logo(image, logo):

    for linha in range(image.shape[0]):
        for coluna in range(image.shape[1]):

            b, g, r = logo[linha, coluna]

            if((b, g, r) < (250, 250, 250)):
                image[linha, coluna] = logo[linha, coluna]
    return image

#a imagem com a logo
logo_background = renderizando_logo(img2Logo)
image = img_logo(img1, logo_background)

#minha mask
mask = cv2.cvtColor(logo_background, cv2.COLOR_RGB2GRAY)
mask = cv2.bitwise_not(mask)


# Aplicar inpainting com a técnica de Telea
inpainted_telea = cv2.inpaint(image, mask, inpaintRadius=10, flags=cv2.INPAINT_TELEA)

# Aplicar inpainting com a técnica NS
inpainted_ns = cv2.inpaint(image, mask, inpaintRadius=5, flags=cv2.INPAINT_NS)


cv2.imshow('Original', image)
cv2.imshow('Inpaint Telea', inpainted_telea)
cv2.imshow('Inpaint NS', inpainted_ns)


cv2.waitKey(0)
cv2.destroyAllWindows()
