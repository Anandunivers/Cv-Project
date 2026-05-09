import cv2 

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    # Region of intrasrt
    roi_gray=gray[y:y+h,x:x+w]

    roi_color=gray[y:y+h,x:x+w]
#  for eye detection 
    eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)

    if len(eyes)>0:
        cv2.putText(frame,"Eye Detected",(x,y-30),cv2.FORMATTER_FMT_DEFAULT,0.6,(0,0,255),2)

# for smilw detection 
    smiles=smile_cascade.detectMultiScale(roi_gray,1.7,20)
    if len(smiles) > 0:
        cv2.putText(frame, "Smiling", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)


    cv2.imshow("Smart Face Detector:",frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cap.release()

cv2.destroyAllWindows()