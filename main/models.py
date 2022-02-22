from django.db import models


class Items(models.Model):
    AGES = [
        (6, '6+'),
        (12, '12+'),
        (16, '16+'),
        (18, '18+')
    ]

    name = models.CharField("Название", max_length=32)
    description = models.TextField('Описание')
    genre = models.CharField("Жанр", max_length=32)
    age = models.IntegerField('Возрастное ограничение', choices=AGES)

    def __str__(self):
        return self.name
