from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from products.serializers import ProductsSerializer


class ProductsApiTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Создает 4 тестовых продукта в базе данных
        """
        Product.objects.create(name='Хлеб', price='30')
        Product.objects.create(name='Сыр', price='200')
        Product.objects.create(name='Колбаса', price='250')
        Product.objects.create(name='Молоко', price='80')

        self.serialized_data = [
            ProductsSerializer(Product.objects.get(pk=1)).data,
            ProductsSerializer(Product.objects.get(pk=2)).data,
            ProductsSerializer(Product.objects.get(pk=3)).data,
            ProductsSerializer(Product.objects.get(pk=4)).data
        ]

    def test_get_list(self):
        """
        Тест GET запроса для получения ListView продуктов.
        Получает список продуктов в базе данных отправляя GET запрос по адресу /product/.
        """
        url = reverse('product-list')
        response = self.client.get(url)
        serialized_data = self.serialized_data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_detailed(self):
        """
        Тест GET запроса для получения DetailView продукта.
        Получает конкретный продукт в базе данных отправляя GET запрос по адресу /product/1.
        """
        url = reverse('product-detail', args=[2])
        response = self.client.get(url)
        serialized_data = self.serialized_data[1]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_post(self):
        """
        Тест POST запроса для добавления продукта в базу данных.
        Добавляет продукт в базу данных отправляя POST запрос по адресу /product/.
        """
        product_json = {"name": "Сыр", "price": 220}
        url = reverse('product-list')
        response = self.client.post(url, product_json)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_put(self):
        """
        Тест PUT запроса для обновления продукта в базе данных.
        Обновляет продукт в базе данных отправляя PUT запрос по адресу /product/1.
        """
        url = reverse('product-detail', args=[3])
        product_json = {'name': 'Колбаса', 'price': 199}
        response = self.client.put(url, product_json)
        serialized_data = ProductsSerializer(Product.objects.get(pk=3)).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_delete(self):
        """
        Тест DELETE запроса для удаления продукта из базы данных.
        Удаляет продукт из базы данных отправляя DELETE запрос по адресу /product/1.
        """
        url = reverse('product-detail', args=[4])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)
