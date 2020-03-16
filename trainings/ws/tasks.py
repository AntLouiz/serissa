from __future__ import absolute_import, unicode_literals
import pickle
import cv2
import face_recognition
from itertools import compress
from datetime import datetime
from serissa.celery import app
from celery import group, chain
from celery.task import subtask
from imutils import paths
from serissa.settings import BASE_DIR
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from serissa.cache import redis_instance


@app.task()
def face_recognition_training(*args, **kwargs):
    group_key = kwargs.get('group_key')
    layer = get_channel_layer()

    dataset_path = BASE_DIR.child("media", "captures")
    filename = BASE_DIR.child(
        "recognitor", "training", "face_recognition.pickle"
    )
    detection_method = 'hog'

    images_paths = list(paths.list_images(dataset_path))

    total = len(images_paths)
    current_progress = 0
    progress_limits = [10, 25, 50, 75, 90]

    known_encodings = []
    matrices = []

    now = datetime.now()

    for i, image_path in enumerate(images_paths):
        matrice = image_path.components()[-2]

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

        current_progress = round((i * 100) / total, 1)
        progress_by_limits = [current_progress < p for p in progress_limits]
        current_limits = list(compress(progress_limits, progress_by_limits))

        if current_limits != progress_limits:
            progress_limits = current_limits
            data = {
                'progress': current_progress,
                'status': "running",
                'time_range': None
            }

            async_to_sync(layer.group_send)(
                group_key,
                {
                    "type": "send.progress",
                    "message": data
                }
            )

    after = datetime.now()
    result = after - now

    data = {
        'progress': 100,
        'status': "finished",
        'time_range': result.total_seconds()
    }

    async_to_sync(layer.group_send)(
        group_key,
        {
            "type": "send.progress",
            "message": data
        }
    )


@app.task()
def set_training_status_to_redis(*args, **kwargs):
    status = kwargs.get('status')
    redis_instance.set('training', status)


@app.task()
def process_training():
    chain(
        set_training_status_to_redis.si(status='running'),
        face_recognition_training.si(group_key='face_recognition'),
        set_training_status_to_redis.si(status='stopped')
    )()
