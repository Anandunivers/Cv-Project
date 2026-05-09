import cv2 

# opne cmara

cam=cv2.VideoCapture(0)

fw=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
fh=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

code=cv2.VideoWriter_fourcc(*'XVID')

recoder=cv2.VideoWriter("My video.mp4",code,20,(fw,fh))


while True:
    success ,image=cam.read()


    if not success:
        print("Video Not Capture :")
        break

    recoder.write(image)
    cv2.imshow("Recodring live",image)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Your video Svae")
        break

cam.release()
recoder.release()
cv2.destroyAllWindows()
