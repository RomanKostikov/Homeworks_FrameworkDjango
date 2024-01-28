# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=70)
    address = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}, email: {self.email}, register date: {self.register_date}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    image_product = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return (f'{self.title}, price: {self.price}, count: {self.count}, add date: {self.add_date}, '
                f'image: {self.image_product}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(
        Product)  # создается автоматически таблица Order_products связи таблиц Order и Product
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.client.name} ordered {self.product} = {self.order_sum}, order date: {self.order_date}'
