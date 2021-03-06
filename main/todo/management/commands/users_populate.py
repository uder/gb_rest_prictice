from django.core.management.base import BaseCommand, CommandError
# from django.core.management import call_command
from todo.models import User
from django.contrib.auth.models import User as DjangoUser


class Command(BaseCommand):
    help='Create superuser and populate several Todo app users'

    def _add_todo_user(self,param_dict):
        User.objects.create(**param_dict)

    def _add_super_user(self):
        DjangoUser.objects.create_superuser('root',email='root@emaple.com',password='rootpass')

    def handle(self,*args, **options):
        self._add_super_user()
        for index in range(3):
            params_dict={}
            params_dict.update({'user_name':f'test{index}'})
            params_dict.update({'first_name':f'firsrt_name{index}'})
            params_dict.update({'last_name':f'last_name{index}'})
            params_dict.update({'email':f'test{index}@example.com'})
            self._add_todo_user(params_dict)