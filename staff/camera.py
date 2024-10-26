# face_recognition/camera.py
import cv2

from staff.models import Staff

class VideoCamera:
    def __init__(self):
        # Initialize the camera
        self.video = cv2.VideoCapture(0)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('recognizers/trainer.yml')  # Load the trained model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        # Release the camera when done
        self.video.release()

    def get_frame(self):
        # Capture frame-by-frame
        success, frame = self.video.read()
        if not success:
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            id_, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 60:
                # Display the recognized ID on the frame
                staff = Staff.objects.get(id=id_)
                cv2.putText(frame, f'{staff.name} {confidence}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            else:
                pass
                # cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            # Draw rectangle around detected face

        # Encode the frame in JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()  # Return the frame as bytes


def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')