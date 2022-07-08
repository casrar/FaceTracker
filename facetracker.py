import cv2 

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Error with camera")
    exit()
while True:
    end, frame = capture.read()

    if not end:
        print("Stream has ended.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()