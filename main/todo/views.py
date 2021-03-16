# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, UpdateModelMixin
# from rest_framework.response import Response
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

class UserGenericViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSreializer