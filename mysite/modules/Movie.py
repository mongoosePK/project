'''
    This class is meant to organize the properties of
    a movie and create an easy to read outline of
    defining the states and components of a Movie

    To include in a project, must added folder/module
    to module path for python to search
    [
        ie.
        import sys
        sys.path.append("relative path")
    ]
'''

class Movie:
    def __init__(self):
        # Constructor
        self._title, self._year, self._mID, self._rating, self._description = ""

    '''
        Getters and Setters for current movie instance
    '''
    # setters
    def setTitle(self, titleIn):
        self._title = titleIn

    def setYear(self, yearIn):
        self._year = yearIn

    def setMovieId(self, movieId):
        self.mID = movieId

    def setRating(self, ratingIn):
        self._rating = ratingIn

    def setDescription(self, descriptionIn):
        self._description = descriptionIn

    # getters
    def getTitle(self):
        return self._title

    def getYear(self):
        return self._year

    def getMovieId(self):
        return self._mID

    def getRating(self):
        return self._rating

    def getDescription(self):
        return self._description


if __name__ == "__main__":
    movie1 = Movie()
    movie1.setTitle("Joker")
    movie1.setYear("2019")
    print(movie1.getTitle)
    print(movie1.getYear)
    
