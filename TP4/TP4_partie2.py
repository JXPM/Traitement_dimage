import cv2
import mediapipe as mp
import numpy as np

# Initialisation de la webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam")
    exit()

# Initialisation de Mediapipe
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)  # Détection plus sensible

# Création d'une fenêtre unique pour l'affichage
cv2.namedWindow("Webcam - Detection centrée avec blur", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire la frame")
        break

    # Conversion en RGB pour Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    h, w, _ = frame.shape
    center_frame = (w // 2, h // 2)
    faces = []

    # Détection des visages
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            x, y, w_box, h_box = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
            x, y = max(0, x), max(0, y)
            faces.append(((x + w_box // 2, y + h_box // 2), (x, y, w_box, h_box)))

    # Identifier le visage principal et flouter les autres
    if faces:
        # Visage principal = le plus proche du centre
        main_face = min(faces, key=lambda f: np.linalg.norm(np.array(f[0]) - np.array(center_frame)))
        main_x, main_y, main_w, main_h = main_face[1]

        # Flouter tous les autres visages
        for _, (x, y, w_box, h_box) in faces:
            face_region = frame[y:y + h_box, x:x + w_box]

            if (x, y, w_box, h_box) != (main_x, main_y, main_w, main_h):
                # Assurer que le floutage est impair
                distance = np.linalg.norm(np.array((x + w_box // 2, y + h_box // 2)) - np.array(center_frame))
                blur_intensity = max(15, int(distance // 10) | 1)
                blurred_face = cv2.GaussianBlur(face_region, (blur_intensity, blur_intensity), 30)
                frame[y:y + h_box, x:x + w_box] = blurred_face

        # Dessiner un rectangle vert autour du visage principal
        cv2.rectangle(frame, (main_x, main_y), (main_x + main_w, main_y + main_h), (0, 255, 0), 2)

    # Affichage unique avec une seule fenêtre
    cv2.imshow("Webcam - Detection centrée avec blur", frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
