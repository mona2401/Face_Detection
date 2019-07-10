import cv2
face_detect=cv2.CascadeClassifier('C:\\Users\\OCAC\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_detect.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Kunu",frame)
    key=cv2.waitKey(1)
    if key==ord('k'):
        break
video.release()
cv2.destroyAllWindows()
