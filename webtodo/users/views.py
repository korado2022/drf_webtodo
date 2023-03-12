from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer, UseraddModelSerializer
# Create your views here.

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UseraddModelSerializer

        return UserModelSerializer