FROM		python:3.6.7-slim

RUN			pip3 install django
COPY		.	/srv/

WORKDIR		/srv/app
CMD			python manage.py runserver 0:8000
