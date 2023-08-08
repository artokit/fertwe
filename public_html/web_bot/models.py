from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(verbose_name='Логотип')

    class Meta:
        verbose_name_plural = 'Марки машин'
        verbose_name = 'марку машины'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/cars/{self.pk}/'


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка машины')
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение машины')

    class Meta:
        verbose_name_plural = 'Машины'
        verbose_name = 'машину'

    def __str__(self):
        return self.name
