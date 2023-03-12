"""webtodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
from graphene_django.views import GraphQLView


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Webtodo",
        default_version='v2',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)




# from webtodo.views import ToDoDjangoFilterViewSet

from .views import ProjectDjangoFilterViewSet, TodoDjangoFilterViewSet, ProjectLimitOffsetPaginationViewSet, \
    TodoLimitOffsetPaginationViewSet, ProjectViewSet, UserCustomViewSet, ToDoViewSet

from rest_framework.authtoken import views

# from userapp.views import UserappListApiView

router = DefaultRouter()
router.register('users', UserModelViewSet)
# router.register('user', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
# router.register('project', ProjectViewSet)
router.register('todos', TodoModelViewSet)
# router.register(r'todo', TodoViewSet, basename='todo')
# router.register('project_f', ProjectDjangoFilterViewSet)
# router.register('project_p', ProjectLimitOffsetPaginationViewSet)
# router.register('todo_f', TodoDjangoFilterViewSet)
# router.register('todo_p', TodoLimitOffsetPaginationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    path('swagger/', schema_view.with_ui('swagger')),
    # path('redoc/', schema_view.with_ui('redoc')),
    # path('api/<str:version>/user/', UserListApiView.as_view())
    path('api/user/v1/', include('userapp.urls', namespace='v1')),
    path('api/user/v2/', include('userapp.urls', namespace='v2')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),


]
