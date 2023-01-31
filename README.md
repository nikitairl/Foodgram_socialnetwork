# github/Nikitairl
## _FOODGRAM - социальная сеть для тех кто любит готовить._

http://130.193.36.134/recipes


[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## FOODGRAM - социальная сеть для тех кто любит готовить.

> Голод укрощает даже льва.

Веб-приложение Foodgram - сервис, который позволит вам делиться рецептами блюд, смотреть рецепты других пользователей, добавлять рецепты в избранное, подписываться на пользователей, а также составлять список продуктов для рецепта и выгружать его в pdf файл.

## Стек:

Django, REST API, PosgreSQL, Docker, Nginx, Git.

## Примеры запросов по API:

- [GET]  /api/users/ - Получить список всех пользователей.
- [POST] /api/users/ - Регистрация пользователя.
- [GET]  /api/tags/ - Получить список всех тегов.
- [POST] /api/recipes/ - Создание рецепта.

# Установка 
Шаблон наполнения env-файла:

- DJANGO_SECRET_KEY = '' секретный ключ Django
- DBUSER = '' - логин для подключения к базе данных Postgres
- DBPASSWORD = '' пароль для подключения к базе данных Postgres
- POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой) 
- DBENGINE = 'django.db.backends.postgresql'

Создание образа:
- Используя терминал перейдите в директорию расположения файла Dockerfile
```docker build -t foodgram .```
