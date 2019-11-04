'''
    This file is meant to create a readable interface to data
    returned from an IMDb request.
'''
class Query:
    def __init__(self, json):
        self._json = json
        
    def getTitle(self):
        return self._json["Title"]
    def getYear(self):
        return self._json["Year"]
    def getPosterURL(self):
        return self._json["Poster"]
    def getId(self):
        return self._json["imdbID"]


class MovieQuery(Query):
    def __init__(self,json):
        super().__init__(json)

    def getRated(self):
        return self._json["Rated"]
    def getReleaseDate(self):
        return self._json["Released"]
    def getRuntime(self):
        return self._json["Runtime"]
    def getGenre(self):
        return self._json["Genre"]
    def getPlot(self):
        return self._json["Plot"]

class SearchQuery(Query):
    def __init__(self, json):
        super().__init__(json)
        
