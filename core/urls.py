from django.contrib import admin
from django.urls import path
from api.views import add_product, get_products, get_product_id,  get_name,  get_color
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add', add_product),
    path('api/get', get_products),
    path('api/get/<int:pk>', get_product_id),
    path('api/get/<str:name>', get_name),
    path('api/get/color/<str:color>', get_color),
    
    
]
