from django.db import models

#Default auto=incrementing primary key
#Make username unique
#Make email unique
#Have a password
#Use username and password to login
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=320)
    name = models.CharField(max_length=50)
