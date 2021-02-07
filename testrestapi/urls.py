from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet

router = SimpleRouter()

router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
