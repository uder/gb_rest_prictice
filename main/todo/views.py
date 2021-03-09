# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User,Project,ToDo
from .serializers import UserModelSreializer,ProjectModelSerializer,ToDoModelSerializer

# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSreializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
