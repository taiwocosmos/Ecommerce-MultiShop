from django.urls import path
from . import views
urlpatterns = [
    path('api/products', views.product_view),
    path('api/product/<int:pk>', views.each_product),
    path('api/products', views.products_list),
    path('api/product/<int:pk>', views.product),
]