# Imports
import sys

# set system path to allow Python to find Request Module
sys.path.append("modules/")

# Include RequestBuilder in current proejct
from RequestBuilder import MovieRequest, SearchRequest

# Create your models here.
# This is where requests will be made via Request.py in modules
class MovieModel:
    def __init__(self, genre):
        searchReq = SearchRequest("Guardians")
        searchReq.makeRequest()

        self._movies = []
        for i in range(9):
            currRequest = MovieRequest()
            currRequest.setMovieId(searchReq.getId(i))
            currRequest.makeRequest()
            
            currObj = {
                "title":currRequest.getTitle(),
                "rated":currRequest.getRated(),
                "runtime":currRequest.getRuntime(),
                 "plot":currRequest.getPlot()
            }
            self._movies.append(currObj)

    def getData(self):
        return self._movies
    
