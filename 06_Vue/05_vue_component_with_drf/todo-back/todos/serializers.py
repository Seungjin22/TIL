from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo


User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

class UserSerializer(serializers.ModelSerializer):
    # 특정 user가 가지고 있는 todo 목록들(여러개 -> many=True)
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set',)