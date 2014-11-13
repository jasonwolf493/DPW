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
        p.title = "Encapsulation"
        p.body = "Some not so creative body text."
        p.css = "css/main.css"
        self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
