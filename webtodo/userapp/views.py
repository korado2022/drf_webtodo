from django.shortcuts import render
from rest_framework.generics import ListAPIView


from userapp.serializers import UserFullModelSerializer, UserShortModelSerializer

from users.models import User


# Create your views here.
class UserappListApiView(ListAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserFullModelSerializer

        return UserShortModelSerializer
