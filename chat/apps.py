# chat/apps.py
from django.apps import AppConfig
from django.db.models import BigAutoField

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

class ChatConfig(AppConfig):
    name = 'chat'
