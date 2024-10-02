import cv2
import os
import numpy as np
from .models import Staff, StaffFace


def train_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = []
    ids = []

    staff_members = Staff.objects.all()

    for staff in staff_members:
        staff_faces = StaffFace.objects.filter(staff=staff)
        for staff_face in staff_faces:
            img_path = staff_face.image.path
            img = cv2.imread(img_path)

            if img is None:
                print(f"Error reading image {img_path}")
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            detected_faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5
            )

            for x, y, w, h in detected_faces:
                face = gray[y : y + h, x : x + w]
                faces.append(face)
                ids.append(staff.id)

    if len(faces) == 0:
        print(f"No faces found for staff member {staff.name}")

    recognizer.train(faces, np.array(ids))

    # create recognizers folder if it doesn't exist
    if not os.path.exists("recognizers"):
        os.makedirs("recognizers")

    recognizer.save("recognizers/trainer.yml")

    print("Training completed and model saved.")
