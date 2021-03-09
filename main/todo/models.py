from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4)
    user_name=models.CharField(max_length=64)
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    email=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user_name

class Project(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64, unique=True)
    repo_url=models.URLField()
    users=models.ManyToManyField(User)

    def __str__(self):
        return self.name

class ToDo(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    text=models.CharField(max_length=32767)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user_creator=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=0)
    active=models.BooleanField()

