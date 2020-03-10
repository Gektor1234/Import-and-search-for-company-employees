from django.db import models

class Workers(models.Model):    # создаем модель в которую будем импортировать спарсиные данные
    name = models.CharField(max_length=255, default=True)
    surname = models.CharField(max_length=255, default=True)
    date_of_birth = models.PositiveIntegerField(default=True)
    position = models.TextField(default=True)

