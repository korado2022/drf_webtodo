from rest_framework.serializers import ModelSerializer

from .models import User

class UserModelSerializer(ModelSerializer):


    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UseraddModelSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')
