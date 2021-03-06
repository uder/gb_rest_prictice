from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    help='drops database'

    def handle(self,*args, **options):
        db_file=os.path.join(os.getcwd(),"main","db.sqlite3")
        os.remove(db_file)