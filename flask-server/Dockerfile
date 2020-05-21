FROM python:3.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /srv/app/flask-server

COPY . /srv/app/flask-server

WORKDIR /srv/app/flask-server

RUN pip install -r requirements.txt

EXPOSE 8000

#CMD ["flask", "run"]

CMD ["gunicorn", "-w 2", "-b", "0.0.0.0:8000" , "app:app"]