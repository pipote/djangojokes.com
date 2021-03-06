from django.urls import path

from .views import JokeListView, JokeDetailView

app_name='jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
]