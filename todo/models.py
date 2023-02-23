from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

class Chats(models.Model):
    prompt = models.CharField(max_length=255)
    response = models.CharField(max_length=255, default="Hello too")
