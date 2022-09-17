from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'author', 'receiver', 'chat')
    list_display = ('author', 'text', 'created_at', 'receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)