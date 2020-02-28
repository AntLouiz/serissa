import re
import pickle
import cv2
import face_recognition
from imutils import paths


def encode_captures():
    # dataset_path = settings.BASE_DIR.child("recognitor", "captures")
    dataset_path = '../captures'
    filename = './face_recognition.pickle'
    detection_method = 'hog'

    images_paths = list(paths.list_images(dataset_path))
    print(images_paths)

    known_encodings = []
    matrices = []

    regex = re.compile(r'\w+/(?P<matrice>\w+)/')

    for i, image_path in enumerate(images_paths):
        print("Processing image {}/{}".format(
            i+1,
            len(images_paths)
        ))
        matrice = regex.search(image_path)['matrice']

        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(
            rgb,
            model=detection_method
        )

        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            known_encodings.append(encoding)
            matrices.append(matrice)

        data = {"encodings": known_encodings, "matrices": matrices}

        with open(filename, 'wb') as f:
            f.write(pickle.dumps(data))


if __name__ == '__main__':
    encode_captures()
