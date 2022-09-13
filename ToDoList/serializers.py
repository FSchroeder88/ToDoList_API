from dataclasses import fields
from django.contrib.auth.models import User
from .models import Todo
from rest_framework import serializers


# Create User Serial for TodoSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ['id','title', 'user', 'task', 'created_at']