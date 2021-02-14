from django.db import models

from testrestapi import settings


class Discount(models.Model):
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    DISCOUNT = (
        (0, 'Нет скидки'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
        (20, '20%'),
        (25, '25%'),
        (30, '30%'),
        (35, '35%'),
        (40, '40%'),
        (45, '45%'),
        (50, '50%'),
    )

    discount_value = models.IntegerField('Скидка в процентах', default=0, choices=DISCOUNT)

    def __str__(self):
        return f'Скидка {self.discount_value} %'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='Название продукта', max_length=50)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, verbose_name='Изображение продукта', blank=True)
    price = models.IntegerField(verbose_name='Цена продукта')
    discount_value = models.ForeignKey(
        Discount, verbose_name='Скидка в процентах', null=True, blank=True, on_delete=models.SET(True)
    )
    discount_price = models.IntegerField(verbose_name='Цена со скидкой', blank=True, default=0)

    def save(self, *args, **kwargs):
        """
        Расчитать стоимость со скидкой
        """
        if self.discount_value:
            self.discount_price = int(self.price * (100 - self.discount_value.discount_value) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
