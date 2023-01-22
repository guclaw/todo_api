from rest_framework import generics
from . import models
from . import serializers


class DetailTodo(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
