from django.db import models


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

    def __str__(self):    return self.title
