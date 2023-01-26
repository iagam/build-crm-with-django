from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=1)
    agent_id = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)


class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
