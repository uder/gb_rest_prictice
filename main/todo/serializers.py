from rest_framework.serializers import HyperlinkedModelSerializer,PrimaryKeyRelatedField,SlugRelatedField,StringRelatedField,ModelSerializer
from .models import User,Project,ToDo
from django.contrib.auth.models import User as DjangoUser

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('user_name', 'first_name', 'last_name', 'email')

class UserModelRoleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('uuid', 'user_name', 'first_name', 'last_name', 'email', 'is_leader', 'is_ops')

class DjangoUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=DjangoUser
        fields=('username', 'last_name', 'email')

class DjangoUserStaffModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=DjangoUser
        fields=('username', 'last_name', 'email', 'is_superuser', 'is_staff')


class ProjectModelSerializer(ModelSerializer):
    users=PrimaryKeyRelatedField(queryset=User.objects.all(),many=True)
    class Meta:
        model=Project
        fields='__all__'

class ToDoModelSerializer(HyperlinkedModelSerializer):
    project=PrimaryKeyRelatedField(queryset=Project.objects.all())
    user_creator=PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=ToDo
        fields=['url','uuid','project','text','created_at','updated_at','user_creator','active']
