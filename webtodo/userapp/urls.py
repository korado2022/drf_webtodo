from django.urls import path
from .views import UserappListApiView


app_name = 'userapp'

urlpatterns = [
    path('', UserappListApiView.as_view()),
]