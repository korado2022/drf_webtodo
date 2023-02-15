from django.db import models

from users.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    link_repo = models.URLField()
    developers = models.ManyToManyField(User)


class ToDo(models.Model):
    working = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_note = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    author_todo = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
