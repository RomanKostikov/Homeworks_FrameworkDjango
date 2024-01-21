from django.core.management.base import BaseCommand

from app_2.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Fetched orders data:'))
        orders = Order.objects.all()

        for order in orders:
            self.stdout.write(f'{self.style.ERROR(order.pk)}: {order}')