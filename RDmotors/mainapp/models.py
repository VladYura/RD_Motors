import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Cars(models.Model):
    name = models.CharField('Марка', max_length=100)
    model = models.CharField('Модель', max_length=100, blank=True)
    url = models.SlugField('url', max_length=100, unique=True, null=True)

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'


class PartCard(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Cars, verbose_name='Авто', on_delete=models.SET_NULL, null=True,
                            related_name='car')
    car_year = models.PositiveIntegerField('Год', default=2000,
                                           validators=[MinValueValidator(1980), MaxValueValidator(2050)])
    article = models.CharField('Артикул', max_length=8, unique=True, default=0)
    published_date = models.DateTimeField('Дата публикации', default=datetime.datetime.now)
    price = models.IntegerField('Цена', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('part-card-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.category} - {self.car}'

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'


class Photo(models.Model):
    part_card = models.ForeignKey(PartCard, verbose_name='Запчасть', on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='photo/')

    def __str__(self):
        return self.part_card.category.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
