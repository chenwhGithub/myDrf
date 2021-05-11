from django.urls import path
from .views import ListView, DetailView

app_name = 'goods'
urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('<int:index>', DetailView.as_view(), name='detail'),
]
