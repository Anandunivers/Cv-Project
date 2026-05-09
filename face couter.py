import cv2

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

# Unique faces list
saved_faces = []

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        # Face center
        cx = x + w // 2
        cy = y + h // 2

        new_face = True

        # Check existing faces
        for (px, py) in saved_faces:

            distance = ((cx - px)**2 + (cy - py)**2)**0.5

            # Agar same area me hai
            if distance < 20:
                new_face = False
                break

        # Save new face
        if new_face:
            saved_faces.append((cx, cy))
            print("New Face Detected!",)

        # Draw rectangle
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # Show unique count
    cv2.putText(
        frame,
        f"Unique Faces: {len(saved_faces)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    cv2.imshow("Unique Face Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()