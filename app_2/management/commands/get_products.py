from django.core.management.base import BaseCommand

from app_2.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Fetched products data:'))
        products = Product.objects.all()

        for product in products:
            self.stdout.write(f'{self.style.ERROR(product.pk)}: {product}')