from __future__ import print_function
import cv2 as cv

    
cont_anterior = 0
qntFace = 0
contou = False


def countImg(frame):
    
    cont = 0
    global cont_anterior

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            cont += (sum(frame[i, j]) // 3)
    cont = cont // (frame.shape[0] * frame.shape[1])

    if abs(cont_anterior - cont) > 15:
        cont_anterior = cont
        return True
    else:
        cont_anterior = cont
        return False

def detectAndDisplay(frame):
    mudouScreen = countImg(frame)

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=6,minSize=(30,30), flags=cv.CASCADE_SCALE_IMAGE)
    global qntFace

    
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

    global contou
    if mudouScreen :
        contou = False

    if len(faces):
        if not contou:
            qntFace += len(faces)
            contou = True
    
    return frame

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv.VideoCapture("img/ifma-480p.avi")


if not capture.isOpened():
    print("Erro ao acessar video")
else:
    frame_number = 0
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            detect_face_frame = detectAndDisplay(frame)
            cv.imshow('Video', detect_face_frame)

            if cv.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break

capture.release()
cv.destroyAllWindows()

print('Quantidade de pessoas identificadas: ', qntFace)
