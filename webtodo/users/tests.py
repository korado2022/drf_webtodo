import math
import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .views import UserModelViewSet
from .models import User
# Create your tests here.

class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin_1'
        self.password = 'admin_1_123456789'
        self.email = 'admin_1@m.ru'

        self.data = {'username': 'Sergey', 'first_name': 'Sergey', 'last_name': 'Sergeev', 'email': 'sergey@m.ru'}
        self.data_put = {'username': 'Aleks', 'first_name': 'Aleks', 'last_name': 'Ashukin', 'email': 'aleks@m.ru'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(username=self.name, password=self.password, email=self.email)

    def test_get_list(self):
        factory = APIRequestFactory()
        # request = factory.get('/api/users/')  # вариант передачи адреса напрямую
        request = factory.get(self.url)         # вариант передачи адреса через переменную
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest_api(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin_api(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_cr = User.objects.get(id=user.id)
        # 'username': 'Aleks', 'first_name': 'Aleks', 'last_name': 'Ashukin', 'email': 'aleks@m.ru'
        self.assertEqual(user_cr.username, 'Aleks')
        self.assertEqual(user_cr.first_name, 'Aleks')
        self.assertEqual(user_cr.last_name, 'Ashukin')
        self.assertEqual(user_cr.email, 'aleks@m.ru')
        client.logout()



    def tearDown(self) -> None:
        pass



class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        response = math.sqrt(4)
        self.assertEqual(response, 2)



class TestUser2ViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin_1'
        self.password = 'admin_1_123456789'
        self.email = 'admin_1@m.ru'

        self.data = {'username': 'Sergey', 'first_name': 'Sergey', 'last_name': 'Sergeev', 'email': 'sergey@m.ru'}
        self.data_put = {'username': 'Aleks', 'first_name': 'Aleks', 'last_name': 'Ashukin', 'email': 'aleks@m.ru'}
        self.data_put2 = {'username': 'Nikolay', 'first_name': 'Nikolay', 'last_name': 'Sklar', 'email': 'nikola@m.ru'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(username=self.name, password=self.password, email=self.email)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        user = User.objects.create(**self.data)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.first_name, 'Aleks')
        self.client.logout()


    def test_put_mixer(self):
        user = mixer.blend(User)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.first_name, 'Aleks')
        self.client.logout()

    def test_put_mixer_field(self):
        user = mixer.blend(User, first_name='Vladimir')
        self.assertEqual(user.first_name, 'Vladimir')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{user.id}/', self.data_put2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.first_name, 'Nikolay')
        self.client.logout()



    def tearDown(self) -> None:
        pass