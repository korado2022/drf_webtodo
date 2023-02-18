from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from django_filters import rest_framework as filters

from todo.models import ToDo, Project
from todo.serializers import ToDoModelSerializer, ProjectModelSerializer
from todo.filters import ProjectFilter

from users.models import User
from users.serializers import UserModelSerializer


class ProjectDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class ToDoDjangoFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_fields = ['working']


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination


class ProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer



class ToDoViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


    def list(self, request):
        request = ToDo.objects.all()
        serializer_class = ToDoModelSerializer(request, many=True)
        return Response(serializer_class.data)


    def create(self, request):
        queryset = ToDo.objects.all()
        serializer_class = ToDoModelSerializer(queryset)
        return Response(serializer_class.data)


    def retrieve(self, request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer_class = ToDoModelSerializer(todo)
        return Response(serializer_class.data)


    def update(self, request, pk=None):
        queryset = ToDo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer_class = ToDoModelSerializer(instance=todo, data=request.data, partial=True)

        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        queryset = ToDo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.status = False
        serializer_class = ToDoModelSerializer(instance=todo, data=request.data, partial=True)

        if serializer_class.is_valid(raise_exception=False):
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

        return Response(serializer_class.data)


#  ListModelMixin, DestroyModelMixin, CreateAPIView, RetrieveAPIView, UpdateAPIView, GenericViewSet
class UserCustomViewSet(ListModelMixin,  RetrieveAPIView, UpdateAPIView, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
