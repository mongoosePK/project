'This file is used to create a request to be sent to the IMDb database'
# imports
import sys

# Include module path for python to search
sys.path.append("../dependencies/")

import requests

class Request:
    _api = "84e37cb7"
    _domain = "http://www.omdbapi.com/?"

    def __init__(self):
        self._json = ""
        self._title = ""
        self._year = None
        self._search_type = ""

        # Create base of url for all IMDb requests
        self.url = Request._domain + "apikey=" + Request._api
        
    def makeRequest(self):
        # Make request to current url
        # Send request
        response = requests.get(self.url)
        
        #and (response.json()["Response"] == "True")
        if (response.status_code == 200):
            if (response.json()["Response"] == 'True'):
                print("Success")
                self._json = response.json()
            else:
                print("Unable to find Request")
        elif response.status_code == 404:
            print("Unable to return resource")
        else:
            print(response.status_code)

    '''
        Setters for data controlled by url and
        shared by all Requests
    '''
    def setTitle(self, tIn):
        self._title = tIn
    def setSearchType(self,srcType):
        # Search type can be: movie, series, episode
        self._search_type = srcType
    def setYear(self, yIn):
        self._year = yIn

    # Allow user to collect search title stored
    def getTitle(self):
        return self._title
    # Allow user to collect search type stored
    def getSearchType(self):
        return self._search_type
    # Allow user to collect year of current Request
    def getYear(self):
        return self._year
    # Allow user to collect data
    def getJSON(self):
        return self._json
            
class SearchRequest(Request):
    def __init__(self, title = "", year = None):
        # Call to parent class
        super().__init__()

        self.setTitle(title)
        self.setYear(year)
        
        # Which page to return out of 100
        self._page_num = 1 # Default page: 1, max: 100
        
    '''
        Setters for data controlled by url and
        specific to the SearchReqest class
    '''
    def setPageNum(self, numMoviesIn):
        self._page_num = numMoviesIn
        
    # Override parent function
    def makeRequest(self):
        # Build URL before making request
        self._build_search_url()
        
        # Make request by calling parent function
        super().makeRequest()
    
    def _build_search_url(self):        
        if self.getTitle() != "":
            self.url = "%s&s=%s" % (self.url, self.getTitle())
        if self.getYear() != None:
            self.url = "%s&y=%d" % (self.url, self.getYear())
        if self.getSearchType() != "":
            #append search type to each url
            self.url = "%s&type=%s" % (self.url, self.getSearchType())

        # append page number to each url
        self.url = "%s&page=%d" % (self.url, self._page_num)
        
class MovieRequest(Request):
    def __init__(self, title = "", year = None):
        # Call to parent class
        super().__init__()

        self.setTitle(title)
        self.setYear(year)
        self._movieID = ""
        self._plot_type = ""

    '''
        Setters for attributes added to url request and
        are specific to the MovieRequest class
    '''
    def setMovieId(self, mId):
        self._movieID = mId
    def setPlotType(self, plotType):
        # Plot type can be: short, full
        self._plot_type = plotType

    # Override parent method
    def makeRequest(self):
        # Build URL before making the request
        self._build_movie_url()
        
        # Make request by calling parent function
        super().makeRequest()
            
    def _build_movie_url(self):

        if self.getTitle() != "":
            self.url = "%s&t=*%s" % (self.url, self.getTitle())
        if self._movieID != "":
            self.url = "%s&i=%s" % (self.url, self._movieID)
        if self.getYear() != None:
            self.url = "%s&y=%d" % (self.url, self.getYear())
        if self.getSearchType() != "":
            self.url = "%s&type=%s" % (self.url, self.getSearchType())
        if self._plot_type != "":
            self.url = "%s&plot=%s" % (self.url, self._plot_type)
        

if __name__ == "__main__":
    req1 = MovieRequest("8 mile")
    req1.setMovieId("tt0298203") # imdbID for 8 mile
    req1.setSearchType("movie")
    req1.setPlotType("short")
    #make request
    req1.makeRequest()
    jsonData = req1.getJSON()
    print(jsonData["Title"])

    req2 = SearchRequest("Guardians")
    req2.setSearchType("movie")
    req2.makeRequest()
    jsonData = req2.getJSON()
    print(jsonData["Search"][0]["Title"])
