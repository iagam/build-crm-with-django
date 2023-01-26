from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=1)
    agent_id = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
