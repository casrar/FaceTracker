import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def identify(frame):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = frame
    face_rect = face_cascade.detectMultiScale(gray, 
    scaleFactor=1.1, minNeighbors=9)
    eye_rect = eye_cascade.detectMultiScale(gray, 
    scaleFactor=1.1, minNeighbors=15)
    for (x,y,w,h) in face_rect:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        cv2.putText(gray, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        for (x,y,w,h) in eye_rect:
            cv2.rectangle(gray, (x,y), (x+w, y+h), (0,0,255), thickness=2)
            cv2.putText(gray, 'Eye', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


    cv2.imshow('frame', gray)

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Error with camera")
    exit()
while True:
    end, frame = capture.read()

    if not end:
        print("Stream has ended.")
        break
    
    identify(frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
