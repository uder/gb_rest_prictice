import json
from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.test import APITestCase,APIClient,APIRequestFactory,force_authenticate
from rest_framework import status
from mixer.backend.django import mixer
from uuid import uuid4

from .views import UserGenericViewSet,UserModelViewSet
from .models import Project,User as TODOUser,ToDo
# Create your tests here.



class TestUserView(TestCase):
    def setUp(self):
        self.admin_name='admin'
        self.admin_pass='123456'
        admin_mail='admin@example.com'
        self.admin=DjangoUser.objects.create_superuser(self.admin_name,admin_mail,self.admin_pass)

    def test_users_list(self):
        factory=APIRequestFactory()
        request=factory.get('/api/user/')
        # admin=DjangoUser.objects.create_superuser('admin','admin@exapmle.com','123456')
        force_authenticate(request,self.admin)
        view=UserGenericViewSet.as_view({'get':'list'})
        response=view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_retrive(self):
        retrive_user=mixer.blend(TODOUser)
        factory=APIRequestFactory()
        request=factory.get(f'/api/user/{retrive_user.uuid}')
        force_authenticate(request,self.admin)
        view=UserGenericViewSet.as_view({'get':'retrieve'})
        response=view(request, pk=retrive_user.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('user_name'), retrive_user.user_name)

    def test_user_update(self):
        factory=APIRequestFactory()
        user=mixer.blend(TODOUser)
        request=factory.patch(f'/api/user/{user.uuid}/', {'email':'newmail@example.com'}, format='json')
        force_authenticate(request,self.admin)
        view=UserGenericViewSet.as_view({'patch':'partial_update'})
        response=view(request, pk=user.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('email'), 'newmail@example.com')





# class TestProjectView(TestCase):
#     def setUp(self):
#         self.users=[]
#         for i in range(1,4):
#             name=f'DRF_test{str(i)}'
#             user=mixer.blend(TODOUser,user_name=name)
#             self.users.append(user)
#             user.save()
#
#         self.admin_name='admin'
#         self.admin_pass='123456'
#         admin_mail='admin@example.com'
#         self.admin=DjangoUser.objects.create_superuser(self.admin_name,admin_mail,self.admin_pass)
#
#     def test_create_project(self):
#         client=APIClient()
#         project=Project(id=100, name='Test_project', repo_url='repo@example.com')
#         # project.users.set(self.users)
#         # project.save()
#         client.login(username=self.admin_name,passwd=self.admin_pass)
#         response=client.post('/api/project/',project)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)