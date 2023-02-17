from django.db import models

class TVshow(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('MELODRAMME', 'MELODRAMME')
    )



    title = models.CharField('Название фильма',max_length=100)
    description = models.TextField('Описание фильма')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колтчество')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    prise = models.PositiveIntegerField('Цена билета', null=True)

    def __str__(self):
        return self.title