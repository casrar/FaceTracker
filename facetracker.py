import cv2 

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def identify(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rect = haar_cascade.detectMultiScale(gray, 
    scaleFactor=1.1, minNeighbors=9)
    for (x,y, w, h) in face_rect:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (0,255,0), thickness=2)

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
#cv2.destroyAllWindow