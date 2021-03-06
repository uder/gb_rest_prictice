from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    def _populate_db(self):
        call_command('makemigrations')
        call_command('migrate')

    def handle(self,*args, **options):
        self._populate_db()
