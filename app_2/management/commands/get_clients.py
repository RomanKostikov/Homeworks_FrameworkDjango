from django.core.management.base import BaseCommand

from app_2.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Fetched clients data:'))
        clients = Client.objects.all()

        for client in clients:
            self.stdout.write(f'{self.style.ERROR(client.pk)}: {client}')