from django.core.management.base import BaseCommand, CommandParser

from app_2.models import Client


class Command(BaseCommand):
    help = 'Delete client'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('client_id', type=int, help='client id')

    def handle(self, *args, **options):
        client_id = options['client_id']

        client = Client.objects.filter(pk=client_id).first()

        self.stdout.write(self.style.ERROR(f'Client {client} deleted'))
        client.delete()