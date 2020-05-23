from rest_framework import generics

from todo.models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
