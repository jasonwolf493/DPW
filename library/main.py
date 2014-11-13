'''
Jason Wolf
11/5/2014
DPW
Python 2
'''
import webapp2
from pages import Page
from library import MovieData, FavoriteMovies

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        lib = FavoriteMovies()
        # THIS SHOULDNT BE HARD CODED FOR PROJECT
    #movie title
    #year movie was made
    #Director of film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986
        md2.director = "David Lynch"
        lib.add_movie(md2)

        p.body = lib.compile_list()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
