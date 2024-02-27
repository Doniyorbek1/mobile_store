from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add', views.add_product),
    path('api/get', views.get_products)
]
