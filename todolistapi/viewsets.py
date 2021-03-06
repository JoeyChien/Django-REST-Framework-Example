from rest_framework import viewsets
from . import models
from . import serializers

class TodoListViewset(viewsets.ModelViewSet):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer
