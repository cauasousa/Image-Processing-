import cv2
import random 
# import sys


capture = cv2.VideoCapture("img\ifma-480p.avi")
img_logo = cv2.imread('img\logo-if-vertical.png')

tam = 0.75
boolAumenteTam = True

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
local_logo_height, local_logo_height = 0, 0

def mudar_tam_logo():

    global tam, img_logo, boolAumenteTam, local_logo_height, local_logo_width, frame_height, frame_width

    img = None

    if tam <= 0.25:
        boolAumenteTam = True
    elif tam >= 0.75:
        boolAumenteTam = False
    
    c = (img_logo.shape[1]* int(frame_height * tam)) // img_logo.shape[0]
    
    if boolAumenteTam:
        tam+=0.01
    else:
        tam-=0.01
        
    img = cv2.resize(img_logo, (int(c), int(frame_height * tam)), interpolation = cv2.INTER_AREA)

    local_logo_width = (frame_width//2) - ((c)//2)
    local_logo_height = (frame_height//2) - ((frame_height * tam)//2)

    return img
        

def juntar_frame_logo(frame):

    global img_height, img_width, local_logo_height, local_logo_width

    img = mudar_tam_logo()
    
    img_height, img_width = img.shape[:2]

    for linha in range(img_height):
        for coluna in range(img_width):
            b, g, r = img[linha, coluna]

            if b < 255 and g < 255 and r < 255 and local_logo_height + linha < frame_height and local_logo_width + coluna < frame_width:
                
                b, g, r = img[linha, coluna]

                frame[int(local_logo_height + linha)][int(local_logo_width + coluna)] = [b, g, r]
        
    return frame    

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')


if not capture.isOpened():
    print("Erro ao acessar video")
else:

    # Desenvolva um código aplicando a logomarca sobre um vídeo de forma que esta deve estar posicionada no centro 
    # e variar de tamanho suavemente para ocupar entre 75% e 25% da altura.  
    # Observe que os frames do vídeo foram borrados utilizando um filtro gaussiano com kernel de tamanho 25.
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            frame_update = juntar_frame_logo(frame)
            cv2.imshow('frame', frame_update)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()