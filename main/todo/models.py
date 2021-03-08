from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4)
    user_name=models.CharField(max_length=64)
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    email=models.CharField(max_length=255, unique=True)

class Project(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64, unique=True)
    repo_url=models.URLField()
    users=models.ManyToManyField(User)

class ToDo(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    text=models.CharField(max_length=32767)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    active=models.BooleanField()

