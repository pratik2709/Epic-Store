from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BaseFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Profile(BaseFields):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    preferences = models.JSONField()

class Games(BaseFields):
    name = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    age_group = models.IntegerField()
    theme = models.CharField(max_length=200)
    violence = models.CharField(max_length=200)

class Attributes(BaseFields):
    attributes = models.JSONField()

