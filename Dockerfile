FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /api

WORKDIR /api

COPY . /api

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential cmake

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
