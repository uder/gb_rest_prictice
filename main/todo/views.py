# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from .models import User,Project,ToDo
from .serializers import UserModelSreializer,ProjectModelSerializer,ToDoModelSerializer
from .filters import ProjectFilter, ToDoFilter
from .pagination import ProjectPagination, ToDoPagination

# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSreializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class=ProjectFilter
    pagination_class = ProjectPagination

class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    pagination_class = ToDoPagination

    def destroy(self,request, pk=None):
        todo_record=get_object_or_404(ToDo,pk=pk)
        todo_record.active=False
        todo_record.save()
        return Response({f"{todo_record}.Active": False})

class UserGenericViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSreializer

