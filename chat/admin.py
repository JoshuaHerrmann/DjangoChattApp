from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin): #das naming für die display classen ist eig immer ModelnameAdmin also hier MessageAdmin
    fields = ('text', 'created_at', 'author', 'receiver', 'chat') #fields zeigt das an wenn man auf ein objekt drückt
    list_display = ('author', 'text', 'created_at', 'receiver') # das was in der models liste steht
    search_fields = ('text',)# suchfunktion sucht in dem jeweiligen part

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_name',)


    
# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)