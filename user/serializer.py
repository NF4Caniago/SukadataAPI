from django.db.models import fields
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['wa', 'email', 'otp']