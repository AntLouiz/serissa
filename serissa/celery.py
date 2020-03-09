from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery

os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "serissa.settings")

app = Celery('serissa')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
