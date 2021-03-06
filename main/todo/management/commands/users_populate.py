from django.core.management.base import BaseCommand, CommandError
from todo.models import User

class Command(BaseCommand):
    help='Populate several Todo app users'

    def _add_todo_user(self,param_dict):
        User.objects.create(**param_dict)

    def handle(self,*args, **options):
        for index in range(3):
            params_dict={}
            params_dict.update({'user_name':f'test{index}'})
            params_dict.update({'first_name':f'firsrt_name{index}'})
            params_dict.update({'last_name':f'last_name{index}'})
            params_dict.update({'email':f'test{index}@example.com'})
            self._add_todo_user(params_dict)