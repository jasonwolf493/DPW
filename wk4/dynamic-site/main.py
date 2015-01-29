from Pages import Page
from data import DataObject
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        p = Page()
        d = DataObject()

        #if we get an input from user(if link is clicked)
        if self.request.GET:
            #then we will set the page var in DataObject to = the input(index, about, ect.)
            d.page = self.request.GET['page']
            #then we will write this..
            self.response.write(p.print_out(d.page))
        #if nothing is given we'll make sure it's set to index so there are no issues displaying things
        else:
            d.page = "index"
            #then just print the index
            self.response.write(p.print_out(d.page))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
