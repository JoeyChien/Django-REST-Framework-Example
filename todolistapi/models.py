from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=15)
    content = models.CharField(max_length=100)


