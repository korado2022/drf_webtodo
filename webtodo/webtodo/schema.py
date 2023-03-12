import graphene
from graphene_django import DjangoObjectType

from todo.models import Project, Todo
from users.models import User


class ProjectType(DjangoObjectType):

    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):

    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TodoType)
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    todo_by_id = graphene.Field(TodoType, id=graphene.Int(required=True))


    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    def resolve_todo_by_id(self, info, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return None


class UserMutation(graphene.Mutation):
    class Arguments:
        last_name = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)


    @classmethod
    def mutate(cls, root, info, last_name, id):
        user = User.objects.get(pk=id)
        user.last_name = last_name
        user.save()

        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
