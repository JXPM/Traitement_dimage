import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam")
    exit()

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire la frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            h, w, _ = frame.shape
            x, y, w_box, h_box = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)

            marge_x = int(w_box * 0.1)
            marge_y = int(h_box * 0.1)

            x = max(0, x - marge_x)
            y = max(0, y - marge_y)
            w_box = min(w, w_box + 2 * marge_x)
            h_box = min(h, h_box + 2 * marge_y)

            roi = frame[y:y + h_box, x:x + w_box]
            roi_blurred = cv2.GaussianBlur(roi, (25, 25), 30)
            frame[y:y + h_box, x:x + w_box] = roi_blurred

            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)

    cv2.imshow("Webcam - Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
