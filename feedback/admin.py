from django.contrib import admin
from .models import UserProfile, Message, Replies

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'subject', 'created']
    readonly_fields = ['name', 'surname', 'subject', 'phone', 'email']


class RepliesAdmin(admin.ModelAdmin):
    list_display = ['message', 'created']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Replies, RepliesAdmin)
