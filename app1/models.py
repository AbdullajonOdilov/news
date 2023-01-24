from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class News(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name
