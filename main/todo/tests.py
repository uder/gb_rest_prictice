from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.test import APITestCase,APIClient,APIRequestFactory,force_authenticate
from rest_framework import status
from mixer.backend.django import mixer

from .views import UserGenericViewSet
from .models import Project,User,ToDo
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
        retrive_user=mixer.blend(User)
        factory=APIRequestFactory()
        request=factory.get(f'/api/user/{retrive_user.uuid}')
        force_authenticate(request,self.admin)
        view=UserGenericViewSet.as_view({'get':'retrieve'})
        response=view(request, pk=retrive_user.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('user_name'), retrive_user.user_name)

    def test_user_update(self):
        factory=APIRequestFactory()
        user=mixer.blend(User)
        request=factory.patch(f'/api/user/{user.uuid}/', {'email':'newmail@example.com'}, format='json')
        force_authenticate(request,self.admin)
        view=UserGenericViewSet.as_view({'patch':'partial_update'})
        response=view(request, pk=user.uuid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('email'), 'newmail@example.com')


class TestProjectView(TestCase):
    def setUp(self):
        self.admin_name='admin'
        self.admin_pass='123456'
        admin_mail='admin@example.com'
        self.admin=DjangoUser.objects.create_superuser(self.admin_name,admin_mail,self.admin_pass)

    def test_projects_list(self):
        client=APIClient()
        client.force_authenticate(user=self.admin)
        response=client.get('/api/project/')
        client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_create(self):
        client=APIClient()
        client.force_authenticate(user=self.admin)
        response=client.post('/api/project/', {'name': 'DRF_TEST_project', 'repo_url': 'http://example.com/test'})
        client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_project_retrive(self):
        project=mixer.blend(Project)
        client=APIClient()
        client.force_authenticate(user=self.admin)
        response=client.get(f'/api/project/{project.id}/')
        client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), project.name)

    def test_project_update(self):
        project=mixer.blend(Project)
        client=APIClient()
        client.force_authenticate(user=self.admin)
        response=client.patch(f'/api/project/{project.id}/',{'name':'DRF_TEST_NewName'})
        client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'DRF_TEST_NewName')

class TestToDoView(APITestCase):
    def setUp(self):
        self.admin_name='admin'
        self.admin_pass='123456'
        admin_mail='admin@example.com'
        self.admin=DjangoUser.objects.create_superuser(self.admin_name,admin_mail,self.admin_pass)


    def test_todo_list(self):
        self.client.force_authenticate(user=self.admin)
        response=self.client.get('/api/todo/')
        self.client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_create(self):
        project=mixer.blend(Project)
        user=mixer.blend(User)
        self.client.force_authenticate(user=self.admin)
        response=self.client.post('/api/todo/', {'project':project.id, 'userCreator':user.uuid,'text':'DRF_TEST_Text'})
        self.client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_todo_retrieve(self):
        project=mixer.blend(Project)
        user=mixer.blend(User)
        todo=mixer.blend(ToDo, user_creator=user, project=project)
        self.client.force_authenticate(user=self.admin)
        response=self.client.get(f'/api/todo/{todo.uuid}/')
        self.client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('text'), todo.text)

    def test_todo_update(self):
        project=mixer.blend(Project)
        user=mixer.blend(User)
        todo=mixer.blend(ToDo, user_creator=user, project=project)
        self.client.force_authenticate(user=self.admin)
        response=self.client.patch(f'/api/todo/{todo.uuid}/',{'text':'DRF_TEST_NewText'})
        self.client.force_authenticate(user=None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('text'), 'DRF_TEST_NewText')
