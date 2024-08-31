import cv2

capture = cv2.VideoCapture("img\ifma-480p.avi")


if not capture.isOpened():
    print("Erro ao acessar video")
else:

    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            frame = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)

            edges = cv2.Canny(frame,90,140)
            
            cv2.imshow('Video', edges)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()