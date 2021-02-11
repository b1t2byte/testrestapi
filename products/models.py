from django.db import models

# TODO добавить таблицу скидок для товаров
# при сохранении товара в админке django скидка должна пересчитываться автоматически


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    # TODO добавить поле цена со скидкой которое будет автоматически пересчитываться
    # из модели скидок

    def __str__(self):
        return self.name
