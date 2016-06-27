from django.db import models
from django.contrib.auth.models import User

from .functions import validate_image

# Create your models here.


class UserProfile(models.Model):
    """
    User profile.
    """

    user = models.OneToOneField(User, related_name="profile")
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('updated',)


class Message(models.Model):
    """
    Message model
    """
    user = models.ForeignKey(User, related_name='messages', blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('-created',)


class Replies(models.Model):
    """
    Relies to message model
    """
    user = models.ForeignKey(User, related_name='my_replies')
    message = models.ForeignKey(Message, related_name='replies')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message.subject

    class Meta:
        ordering = ('-created',)
