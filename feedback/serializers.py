from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message, UserProfile, Replies


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'description', 'created', 'updated')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'email', 'phone', 'name', 'surname', 'text', 'created', 'updated', 'image', 'pk')


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ('user', 'message', 'text', 'created', 'updated', 'pk')
