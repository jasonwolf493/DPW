__author__ = 'Jason'

class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

        #  have an array to hold the movie info
        #  some way to add to that array
        #  generate a list of movies
        #  calculate time span between movies

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title

    def compile_list(self):
        output = ''
        for movie in self.__movie_list:  # for each movie in the movie array
            output += 'Title: ' + movie.title + '</br>'
        return output


class MovieData(object): #  Data object
    def __init__(self):
        self.title = ''
        self.__year = 0
        self.director = ''

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y