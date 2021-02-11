from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from products.serializers import ProductsSerializer


def create_product(name, price):
    # TODO где docstring к методу ?
    # TODO это нужно перенести в setUp класса ProductsApiTestCase
    return Product.objects.create(name=name, price=price)


class ProductsApiTestCase(APITestCase):
    def test_get_list(self):
        # TODO где docstring к методу ?
        product_1 = create_product(name='Колбаса', price=250)
        product_2 = create_product(name='Кофе', price=200)
        url = reverse('product-list')
        response = self.client.get(url)
        serialized_data = ProductsSerializer([product_1, product_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_detailed(self):
        # TODO где docstring к методу ?
        product_1 = create_product(name='Сыр', price=220)
        url = reverse('product-detail', args=[1])
        response = self.client.get(url)
        serialized_data = ProductsSerializer(product_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_post(self):
        # TODO где docstring к методу ?
        product_json = {"name": "Сыр", "price": 220}
        url = reverse('product-list')
        response = self.client.post(url, product_json)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_put(self):
        # TODO где docstring к методу ?
        # TODO переменная product где используется?
        product = create_product(name='Сыр', price=220)

        # TODO во всем проект кавычки должны быть одинаковые, например одинарные ''
        product_json = {"name": "Молоко", "price": 200}  # TODO тут двойные кавычки
        url = reverse('product-detail', args=[1])
        response = self.client.put(url, product_json)
        serialized_data = ProductsSerializer(Product.objects.get(pk=1)).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_delete(self):
        # TODO где docstring к методу ?
        # TODO переменная product где используется?
        product = create_product(name='Сыр', price=220)

        url = reverse('product-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)
