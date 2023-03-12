from rest_framework import serializers

from rest_framework.serializers import ModelSerializer

from users.models import User


# from .models import User

class UserShortModelSerializer(ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name')


class UserFullModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
