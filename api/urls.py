from django.urls import path

from .views import TodosAPIView, TodoAPIView

urlpatterns = [
    path('todos/', TodosAPIView.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoAPIView.as_view(), name='todo')
]
