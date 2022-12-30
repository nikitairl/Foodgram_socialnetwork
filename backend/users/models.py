from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username: str = models.CharField(
        db_index=True,
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя',
        help_text='Введите уникальное имя пользователя',
    )
    email: str = models.EmailField(
        db_index=True,
        max_length=254,
        unique=True,
        verbose_name='Электронная почта',
        help_text='Введите электронную почту'
    )
    first_name: str = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Имя пользователя',
    )
    last_name: str = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Фамилия пользователя'
    )

    USERNAME_FIELD: email = 'email'
    REQUIRED_FIELDS: str = ['username', 'first_name', 'last_name', 'password']

    def __str__(self) -> str:
        return self.username