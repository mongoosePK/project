from django.shortcuts import render

import sys
sys.path.append("imdb/")
# include model to handle Movie Requests
from models import MovieModel

# Create your views here.
def home(request):
    genreData = MovieModel("horror")
    return render(request, "movie_display.html", {"currUserData": genreData.getData()})
