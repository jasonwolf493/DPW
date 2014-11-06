'''
Jason Wolf
11/5/2014
DPW
Python 2
'''
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
