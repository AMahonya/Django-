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


class News(models.Model):
    title = models.CharField(max_length=100, help_text="Заголовок новости")
    content = models.TextField(help_text="Содержание новости")
    date = models.DateTimeField(auto_now_add=True, help_text="Дата публикации")


class Category(models.Model):
    category_name = models.CharField(max_length=255, help_text="Название категории игры")

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'


class Order(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Игра добавленная в корзина")
    quantity = models.IntegerField(help_text="колличество")
    order_date = models.DateField(help_text="дата в формате гггг-мм-дд")
    status = models.CharField(max_length=255, help_text="статус заказа")

    def __str__(self):
        return f"Order for {self.game.title} x {self.quantity}"

    class Meta:
        db_table = 'order'
