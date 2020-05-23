from django.urls import path

from .views import TodoAPIView

urlpatterns = [
    path('todos/', TodoAPIView.as_view(), name='todos')
]
