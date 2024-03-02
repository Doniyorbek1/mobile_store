from django.contrib import admin
from django.urls import path
from api.views import add_product, get_products
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add', add_product),
    path('api/get', get_products),
]
