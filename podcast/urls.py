from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('podcast/<int:podcast_id>/', views.episodes, name='episodes'),
    path('favorite/', views.favorite, name='favorite'),
]
