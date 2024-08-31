import cv2
import random 
# import sys


capture = cv2.VideoCapture("img\ifma-480p.avi")
img = cv2.imread('img\logo-if-vertical.png')
qnt_frame = 0

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

img = cv2.resize(img, (int(frame_height * 0.2), int(frame_width*0.2)), interpolation = cv2.INTER_AREA)
img_height, img_width, = img.shape[:2]

#escolher local aletaorio 
# ponto_aleatorio = [img_height, img_width]
local_logo_width = random.randint(0, int(int(frame_width) * 0.70))
local_logo_height = random.randint(0, int(int(frame_height) * 0.70))



def mudar_logo():
    global qnt_frame, local_logo_height, local_logo_width

    if qnt_frame  == 100:

        local_logo_width = random.randint(0, int(int(frame_width) * 0.75) - 1)
        local_logo_height = random.randint(0, int(int(frame_height) * 0.75) - 1)
        qnt_frame = 0


cv2.imshow('Cinza', img)
# cv2.waitKey(0)   
# cv2.destroyAllWindows()

def juntar_frame_logo(frame):

    global img, img_height, img_width, local_logo_height, local_logo_width

    for linha in range(img_height):
        for coluna in range(img_width):
            r, g, b = img[linha, coluna]

            if local_logo_height + linha < frame_height and local_logo_width + coluna < frame_width:

                if (245, 245, 245) < (r, g, b):
                    continue
                

                frame[local_logo_height + linha-1, local_logo_width + coluna-1] = [r, g, b]
        
    return frame    

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
output = cv2.VideoWriter("Video_com_logos.mp4", fourcc, int(fps), (int(frame_width), int(frame_height)), True)


if not capture.isOpened():
    print("Erro ao acessar video")
else:
    
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            qnt_frame += 1
            mudar_logo()
            frame_update = juntar_frame_logo(frame)
        
            output.write(frame_update)
            cv2.imshow('Cinza', frame_update)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',frame_update)
            
        else: break

capture.release()
output.release()
cv2.destroyAllWindows()