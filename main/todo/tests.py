from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.test import APITestCase,APIClient,APIRequestFactory,force_authenticate
from rest_framework import status

from .views import UserGenericViewSet,UserModelViewSet

# Create your tests here.


class TestUserView(TestCase):
    def test_users_list(self):
        factory=APIRequestFactory()
        request=factory.get('/api/user/')
        admin=DjangoUser.objects.create_superuser('admin','admin@exapmle.com','123456')
        force_authenticate(request,admin)
        view=UserGenericViewSet.as_view({'get':'list'})
        response=view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
