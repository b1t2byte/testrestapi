from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductsSerializer


# TODO тут создать view (без django-rest) для отображения детальной
# товаров и списка товаров + добавить test case для проверки работоспособности


class ProductViewSet(ModelViewSet):
    # TODO где docstring к классу ?
    # TODO этот класс перенести в api.py
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
