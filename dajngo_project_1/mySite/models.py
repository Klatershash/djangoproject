from django.db import models

class Food:
    title = models.CharField(max_length=100, verbose_name='Название блюда: ')
    description = models.TextField(verbose_name='Описание')
    ings = models.CharField(max_length=100, verbose_name='Ингридиенты: ')
    time = models.IntegerField(verbose_name='Время приготовления: ')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена:')
    image = models.ImageField(upload_to='images', verbose_name='Фото блюда')

# Create your models here.
