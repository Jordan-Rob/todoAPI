from rest_framework import generics

from todo.models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodosAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
