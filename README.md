# github/Nikitairl
## _FOODGRAM - социальная сеть для тех кто любит готовить._


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
