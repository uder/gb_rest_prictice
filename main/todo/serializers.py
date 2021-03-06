from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

class UserModelSreializer(HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('user_name', 'first_name', 'last_name', 'email')
