import cv2
import face_recognition
import pickle
from serissa.settings import BASE_DIR


def recognize_face(image):
    detection_method = 'hog'
    encodings_file_path = BASE_DIR.child(
        "recognitor", "trains", "face_recognition.pickle"
    )

    matrice = None
    confidence = 0

    with open(encodings_file_path, 'rb') as f:
        data = pickle.loads(f.read())

    boxes = face_recognition.face_locations(
        image,
        model=detection_method
    )

    roi = cv2.resize(image, (280, 280))
    faces_encodings = face_recognition.face_encodings(roi, boxes)

    for encoding in faces_encodings:
        matches = face_recognition.compare_faces(
            data['encodings'],
            encoding
        )

        if True in matches:
            matched_ids = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matched_ids:
                matrice = data['matrices'][i]
                counts[matrice] = counts.get(matrice, 0) + 1

            matrice = max(counts, key=counts.get)
            confidence = counts[matrice]

            break

    return matrice, confidence
