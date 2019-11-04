'''
    This class is meant to organize the properties of
    a movie and create an easy to read outline of
    defining the states and components of a Movie
'''
from typing import List
class Movie:
    def __init__(self):
        # Constructor
        self._title = ""
        self._year = None
        self._mID = ""
        self._rating = ""
        self._release_date = ""
        self._runtime = None
        self._genre = ""
        self._description = ""
        self._poster_url = ""

    '''
        Getters and Setters for current movie instance
    '''
    # setters
    def setTitle(self, titleIn:str):
        self._title = titleIn

    def setYear(self, yearIn:int):
        self._year = yearIn

    def setMovieId(self, movieId:str):
        self.mID = movieId

    def setRatings(self, ratings:List[str]):
        # This contains the arrays of different sources rating the
        #   current movie
        self._rating = ratings

    def setReleaseDate(self, rDate:str):
        self._realease_date

    def setRuntime(self, runtime:int):
        # Runtime is store as an int representing number of minutes
        self._runtime

    def setGenre(self, genre:str):
        self._genre = genre
        
    def setDescription(self, description:str):
        self._description = description

    def setPosterURL(self, url:str):
        self._poster_url = url

    # getters
    def getTitle(self):
        return self._title

    def getYear(self):
        return self._year

    def getMovieId(self):
        return self._mID

    def getRatings(self):
        return self._rating

    def getRealaseDate(self):
        return self._release_date

    def getRuntime(self):
        # Runtime is stored in minutes
        return self._runtime

    def getGenre(self):
        return self._genre
    
    def getDescription(self):
        return self._description

    def getPosterURL(self):
        return self._poster_url


if __name__ == "__main__":
    movie1 = Movie()
    movie1.setTitle("Joker")
    movie1.setYear("2019")
    reviews = ["Great", "It sucked", "Best movie ever"]
    movie1.setRatings(reviews)
    for rating in movie1.getRatings():
        print(rating)
    print(movie1.getTitle())
    print(movie1.getYear())
    
