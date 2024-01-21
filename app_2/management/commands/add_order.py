from django.core.management.base import BaseCommand, CommandParser

from app_2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('client_id', type=int, help='Client id')
        parser.add_argument('product_id', type=int, help='Product id')

    def handle(self, *args, **options) -> None:
        client_id = options['client_id']
        product_id = options['product_id']

        client = Client.objects.get(id=client_id)
        product = Product.objects.get(id=product_id)

        order = Order(
            client=client,
            product=product,
            order_sum=product.price * product.count
        )
        order.save()
        self.stdout.write(self.style.SUCCESS(f'Added new order: {order}'))