from django.db import models
from django.db.models import Model


class Post(models.Model):
    GENRE = (
        ('DETECTIVE', 'DETECTIVE'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
    )

    title = models.CharField('Название фильма',max_length=100)
    description = models.TextField('Описание фильма')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колтчество', null=True)
    genre = models.CharField(max_length=100, null=True)
    video = models.URLField(null=True)
    prise = models.PositiveIntegerField('Цена', null=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    choice_book = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name='comment_object')

    rate = models.IntegerField()
    created_data = models.DateTimeField(auto_now_add=True)

