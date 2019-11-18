from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import sys
sys.path.append("imdb/")
# include model to handle Movie Requests
#from models import MovieModel
from imdb_dummy_data import MOVIE_REQUEST_DUMMY_DATA

# Create your views here.
@login_required
def home(request):
    #genreData = MovieModel("horror")
    movie_list = (MOVIE_REQUEST_DUMMY_DATA)
    return render(request, "movie_display.html", {"searchResult": movie_list,"userSearch":"Guardians"})#genreData.getData()})

