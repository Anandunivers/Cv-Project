import cv2

# Face detector load
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Camera start
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    face_count=len(faces)

    # Track faces
    for (x, y, w, h) in faces:

        # Rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Center point
        cx = x + w // 2
        cy = y + h // 2

        # Draw center dot
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        
        # Count face :
        cv2.putText(frame,f"Total Number face:{face_count}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

        # Show coordinates
        cv2.putText(
            frame,
            
            f"X:{cx} Y:{cy}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    cv2.imshow("Live Face Tracking", frame)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()