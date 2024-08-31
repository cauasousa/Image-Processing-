import cv2
import numpy as np
import random 

pontosMatriz = list()
pontosMatriz=[[15, 15]]

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]
frame = None
index_color = 0

def draw_frame():
    for coord in pontosMatriz:
        global frame, index_color
        cv2.circle(frame,(coord[0],coord[1]),3,COLORS[index_color],-1)


def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        
        global pontosMatriz
        add = [x, y]
        pontosMatriz.append(add)
        

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro ao acessar camera ou abrir o vídeo")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv2.CAP_PROP_FPS)
    video = cv2.VideoWriter(filename="video.avi", fourcc = fourcc, fps= fps, frameSize=(frame_width, frame_height), isColor=True)
    
    while capture.isOpened():

        ret, frame = capture.read()
        
        if ret is True:
            
            draw_frame()
            cv2.imshow('Input', frame)
            cv2.namedWindow('Input')
            cv2.setMouseCallback('Input', draw_circle)
            video.write(frame)
            
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            if cv2.waitKey(30) & 0xFF == ord('c'):
                
                aux = index_color
                while aux == index_color:
                    index_color = random.randint(0,len(COLORS)-1)

            if cv2.waitKey(30) & 0xFF == ord(' '):
                pontosMatriz.clear()

        else: break

    video.release()


capture.release()
cv2.destroyAllWindows()
