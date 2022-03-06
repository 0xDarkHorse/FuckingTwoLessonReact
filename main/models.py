from django.db import models


class Users(models.Model):
    email = models.EmailField(primary_key=True, default='')
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

