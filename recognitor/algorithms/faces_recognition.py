import face_recognition
import pickle
from serissa.settings import BASE_DIR


def detect_faces(image):
    detection_method = 'hog'
    boxes = face_recognition.face_locations(
        image,
        model=detection_method
    )

    return boxes


def recognize_face(image):
    detection_method = 'hog'
    encodings_file_path = BASE_DIR.child(
        "recognitor", "training", "face_recognition.pickle"
    )

    matrice = None
    confidence = 0

    with open(encodings_file_path, 'rb') as f:
        data = pickle.loads(f.read())

    boxes = face_recognition.face_locations(
        image,
        model=detection_method
    )

    # roi = cv2.resize(image, (280, 280))
    faces_encodings = face_recognition.face_encodings(image, boxes)

    for encoding in faces_encodings:
        matches = face_recognition.compare_faces(
            data['encodings'],
            encoding
        )
        distance = face_recognition.face_distance(
            data['encodings'],
            encoding
        )[0]

        if True in matches:
            matched_ids = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matched_ids:
                matrice = data['matrices'][i]
                counts[matrice] = counts.get(matrice, 0) + 1

            matrice = max(counts, key=counts.get)
            confidence = round(distance, 2)

            break

    return matrice, confidence
