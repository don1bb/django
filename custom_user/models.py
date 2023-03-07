from random import choices
from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, 'VIPClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)

HIGHER = 1
AVERAGE = 2

EDUC_TYPE = (
    (HIGHER, 'HIGHER'),
    (AVERAGE, 'AVERAGE'),
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя ')
    phone_number = models.CharField('номер телефона', max_length=20)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='пол')
    education = models.CharField(choices=EDUC_TYPE, max_length=20,null=True)
    height = models.CharField('рост', max_length=20, null=True)
    weight = models.CharField('вес', max_length=20,null=True)
    hobby = models.CharField('хобби' , max_length=20,null=True)
    favorite_food = models.CharField('любимая еда', max_length=20, null=True)
    favorite_sport = models.CharField ('любимый спорт', max_length=20, null=True)

