# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from .models import User,Project,ToDo
from django.contrib.auth.models import User as DjangoUser
from .serializers import UserModelSerializer,UserModelRoleSerializer, ProjectModelSerializer, ToDoModelSerializer,DjangoUserModelSerializer,DjangoUserStaffModelSerializer
from .filters import ProjectFilter, ToDoFilter
from .pagination import ProjectPagination, ToDoPagination
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

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
    queryset = User.objects.all().order_by('uuid')
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == "2":
            serializer=UserModelRoleSerializer
        else:
            serializer=UserModelSerializer

        return serializer

class DjangoUserGenericViewSet(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = DjangoUser.objects.all().order_by('id')
    serializer_class = DjangoUserStaffModelSerializer

    def get_serializer_class(self):
        if self.request.version == "2":
            serializer = DjangoUserStaffModelSerializer
        else:
            serializer = DjangoUserModelSerializer

        return serializer

schema_view=get_schema_view(
    openapi.Info(
        title='ToDo',
        default_version='1',
        description="Todo API schema docs",
        # contact="admin@example.com",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
