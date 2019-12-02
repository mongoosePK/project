from django.urls import path
from . import views

urlpatterns = [
    #
    path('movie_search', views.movie_search, name='movie-search'),
    #path('display/', views.display, name='display')
    path('movie_display', views.movie_display, name='movie-display')
]