from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),  # вывод главной страницы
    path('shop/products/', views.products, name='products'),  # вывод списка всей продукции
    path('shop/product/<int:id_product>', views.product, name='product'),
    # вывод выбранного пользователем продукта по id
    path('shop/clients/', views.clients, name='clients'),  # вывод всех клиентов
    path('shop/orders/', views.orders, name='orders'),  # вывод всех заказов
    path('shop/client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    # все заказы по клиенту (формы выбора клиента пока нет)
    path('shop/client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted,
         name='client_products_sorted'),
    # вывод всех товаров по клиенту за указанное кол дней (формы ввода id клиента и кол дней)

]
