from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class User(models.Model):
    wa = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    otp = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

