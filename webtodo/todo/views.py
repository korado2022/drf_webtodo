from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, BasePermission

from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


# class StaffOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_staff

class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [StaffOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [StaffOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer