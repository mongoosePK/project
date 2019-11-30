from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SearchForm
# Create your views here.

movieData = None

#home view returns the basic search page of the app
#the search form is brought in here
@login_required
def home(request):
    form = SearchForm()
    context = { "form": form }
    return render(request, "movie_search.html", context)

#display view 
@login_required
def display(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            searchVal = form.cleaned_data.get('query', '')

        global movieData
        movieData = searchRequest(form) 
        # ^^^^^^ put this in search.py 
        #to be built soon