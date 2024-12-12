from django.db import models
from decimal import Decimal


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=25, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=70, help_text="Название игры")
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), help_text="Цена")
    size = models.DecimalField(max_digits=6, decimal_places=3, default=Decimal('0.00'), help_text="Размер файлов в GB")
    description = models.TextField(help_text="Описание игры")
    age_limited = models.BooleanField(default=False, help_text="Ограничение по возрасту 18+")
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title
