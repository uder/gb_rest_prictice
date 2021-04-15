import graphene
from graphene_django import DjangoObjectType
from .models import User,Project,ToDo

class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class UserType(DjangoObjectType):
    class Meta:
        model=User
        fields='__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model=Project
        fields='__all__'



class Query(graphene.ObjectType):
    all_todo=graphene.List(ToDoType)
    all_user=graphene.List(UserType)

    def resolve_all_todo(self, info):
        return ToDo.objects.all()

    def resolve_all_user(self, info):
        return User.objects.all()


# class Query(graphene.ObjectType):
#     hello=graphene.String(default_value="Hi!")


schema=graphene.Schema(query=Query)