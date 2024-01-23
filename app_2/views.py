from django.shortcuts import render
from django.http import HttpResponse
import logging
from app_2.models import Client, Product, Order
from datetime import datetime, timedelta
from django.shortcuts import render

logger = logging.getLogger(__name__)  # переменная для логирования


# Create your views here.

def index(request):
    return render(request, 'app_2/index.html')


# вывод всех товаров
def products(request):
    products = Product.objects.all()
    logger.info(f'Страница "Список продуктов" успешно открыта')
    return render(request, 'app_2/products.html', {'products': products})


# вывод списка всех клиентов
def clients(request):
    clients = Client.objects.all()

    logger.info(f'Страница "Список клиентов" успешно открыта')
    return render(request, 'app_2/clients.html', {'clients': clients})


# вывод списка заказов
def orders(request):
    products_all = []
    orders = Order.objects.all()

    context = {
        'orders': orders
    }
    return render(request, 'app_2/orders_all.html', context=context)


def client_orders(request, id_client: int):
    products = {}

    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(client=client).all()

    for order in orders:
        products[order.id] = str(order.product.all()).replace('<QuerySet [<', '').replace('>]>',
                                                                                          '').split('>, <')

    return render(request, 'app_2/client_orders.html', {'client': client, 'orders': orders,
                                                        'products': products})


def product(request, id_product: int):
    product = Product.objects.filter(pk=id_product).first()
    context = {
        "product": product

    }
    return render(request, "app_2/product.html", context=context)


def client_products_sorted(request, id_client: int, days: int):
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(client=client, order_date__range=(before, now)).all()
    for order in orders:
        products = order.product.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'app_2/client_all_products_from_orders.html',
                  {'client': client, 'product_set': product_set, 'days': days})
