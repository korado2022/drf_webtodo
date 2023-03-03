from django.test import TestCase
from mixer.backend.django import mixer
from mixer.backend.sqlalchemy import mixer

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from users.models import User

from .models import Project


# Create your tests here.

class TestProjectViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin_1'
        self.password = 'admin_1_123456789'
        self.email = 'admin_1@m.ru'

        self.data_proj = {'title': 'project_1', 'link_repo': 'https://github.com/marselester/django-todo', 'developers': [1]}
        self.data_proj_put = {'title': 'project_2', 'link_repo': 'https://github.com/marselester/django-work', 'developers': [1]}

        self.data_user = {'username': 'Sergey', 'first_name': 'Sergey', 'last_name': 'Sergeev', 'email': 'sergey@m.ru'}

        self.url = '/api/projects/'
        self.admin = User.objects.create_superuser(username=self.name, password=self.password, email=self.email)


    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        user = User.objects.create(**self.data_user)
        proj = Project.objects.create(title='project_1', link_repo='https://github.com/marselester/django-todo')
        proj.developers.set([user.id])
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{proj.id}/', self.data_proj_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        proj_ = Project.objects.get(id=proj.id)
        self.assertEqual(proj_.title, 'project_2')
        self.client.logout()




    def tearDown(self) -> None:
        pass