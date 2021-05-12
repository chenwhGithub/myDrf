from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('<int:index>', DetailView.as_view(), name='detail'),
]
