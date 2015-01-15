
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        p = Page()
        self.response.write(p.build_page())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
