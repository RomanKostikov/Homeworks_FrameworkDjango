## Homework 2

### task001:

Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
*Допишите несколько функций CRUD для работы с
моделями по желанию. Что по вашему мнению актуально в
такой базе данных.

#### Описание решения

Все модели содержат поля из задания. Во всех моделях переопределён метод __str__.

В командах добавил CRUD-операции для работы с моделями:

Create: add_client, add_product, add_order
Read: get_clients, get_products, get_orders
Delete: delete_client

## Homework 3

### task001:

Доработаем задачу 8 из прошлого семинара про клиентов,
товары и заказы.
Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
Подготовьте необходимый маршрут и представление.
Продолжаем работать с товарами и заказами.
Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
*Товары в списке не должны повторятся.

#### Описание решения

1. Создание представления client_orders в views.py - для выдачи на страницу всех заказов со списком товара выбранного
   клиента;
2. Создание представления client_products_sorted в views.py - для выдачи на страницу отсортированного списка товаров по
   времени;
3. Создание маршрутов для этих представлений;
4. Создание шаблона базового base.html в папке templates;
5. Создание шаблонов для выше перечисленных представлений: client_all_products_from_orders.html, client_orders.html.

## Homework 4

### task001:

Задание №6
Доработаем задачу про клиентов, заказы и товары из
прошлого семинара.
Создайте форму для редактирования товаров в базе
данных.

### task002:

Измените модель продукта, добавьте поле для хранения
фотографии продукта.
Создайте форму, которая позволит сохранять фото.

#### Описание решения

1. Выполняем начальные команды

- venv\Scripts\activate.ps1 - активируем venv(если это не сделано по умолчанию)
- python -m pip install Pill - для работы c изображениями

2. В models.py изменяем модель, дописываем поле img

- python manage.py makemigrations app_2
- python manage.py migrate

3. В settings.py прописываем каталоги для хранения изображений:

- MEDIA_URL = '/media/' MEDIA_ROOT = BASE_DIR / 'media'

4. Пишем код в views.py класс Product_form для формы для ввода данных о продукте
5. Прописываем маршрут к view
6. Пишем шаблон product_form.html
7. Запускаем сервер и заполняем форму. Изображение сохранилось в папку.

## Homework 5

### task001:

(Аналогично тому, что делали на семинаре)
Настройте под свои нужды админку вывод информации о клиентах,
товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.

#### Описание решения

1. Создали супепользователя: логин admin, пароль admin
2. Создали в админке группы: Сlients, Orders, Products
3. Создали в админке пользователей: account_manager, orders_manager, products_manager, 
   (пароли одинаковые: GeekBraines2024)
4. В admin.py - прописали подключение админки к моделям
5. В admin.py - прописали персонализацию в админке для каждой таблицы (модели)
