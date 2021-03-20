from rest_framework.serializers import HyperlinkedModelSerializer,PrimaryKeyRelatedField,SlugRelatedField,StringRelatedField,ModelSerializer
from .models import User,Project,ToDo

class UserModelSreializer(HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('user_name', 'first_name', 'last_name', 'email')

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
        fields='__all__'