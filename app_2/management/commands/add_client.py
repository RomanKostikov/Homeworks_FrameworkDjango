from django.core.management.base import BaseCommand, CommandParser

from app_2.models import Client


class Command(BaseCommand):
    help = 'Create user'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options) -> None:
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']
        client = Client(name=name, email=email, phone=phone, address=address)
        self.stdout.write(self.style.SUCCESS(f'Added new client: {client}'))
        client.save()