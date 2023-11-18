from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название блюда: ')
    description = models.TextField(verbose_name='Описание')
    ings = models.CharField(max_length=100, verbose_name='Ингридиенты: ')
    time = models.IntegerField(verbose_name='Время приготовления: ')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена:')
    image = models.ImageField(upload_to='images', verbose_name='Фото блюда')

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    description = models.CharField(max_length=200, verbose_name='Описание статьи')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='mySite/static/blog', verbose_name='Картинка статьи')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class User(models.Model):
    nickname = models.CharField(max_length=200, verbose_name = 'Имя пользователя')
    login = models.CharField(max_length=200, verbose_name = 'Логин пользователя')
    password = models.CharField(max_length=200, verbose_name = 'Пароль пользователя')

    def __str__(self):
        return self.login