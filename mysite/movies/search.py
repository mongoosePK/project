import requests
import json
from .forms import *
from .models import Movie


def movieRequest(form):
    
    if form.is_valid():
        searchVal = form.cleaned_data.get('query', '')
    
    # create a list to hold the movies after we get the relevant data
    searchResults = list()
    url = f'http://omdbapi.com/?apikey=84e37cb7&s={searchVal}&type=movie'
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        json = response.json()
        movie = json['Search']
        for each in movie:
            each = Movie(title = each['Title'], year = each['Year'], mID = each['imdbID'], posterURL = each['Poster'])
            searchResults.append(each)
    # send the list back to the view w/ data to be rendered in HTML
    return searchResults
