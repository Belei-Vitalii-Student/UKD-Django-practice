# Django project for convert png files into jpg

This django project created for converting user png files into jpg files where you can change background color.

Package that was used:
- python:3.11.3
- django:4.2.1
- PostgreSQL 15
- gunicorn:20.1.0
- psycopg2-binary:2.9.6
- nginx
- pillow

## Required software

- python 3.9.16
- pipenv
- Docker Desktop

## Useful command

Run project (site will be available on http://127.0.0.1:8088/)
```sh 
docker compose up --build
```

Check docker image status and ports
```sh 
docker-compose ps
```

Run database migrations
```sh 
docker compose exec django python manage.py migrate 
```

## Some screenshots from site

![image](https://github.com/Belei-Vitalii-Student/UKD-Django-practice/assets/99961129/eb775020-2a53-4141-975f-881d79a98518)
![image](https://github.com/Belei-Vitalii-Student/UKD-Django-practice/assets/99961129/90813cc3-f946-4699-bbef-4a4916b9100f)
![image](https://github.com/Belei-Vitalii-Student/UKD-Django-practice/assets/99961129/e43bf443-b55f-49a3-a565-3e9e666cc703)
