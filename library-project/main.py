'''
Jason Wolf
11/5/2014
DPW
Python 2
'''
import webapp2


from pages import Page
from library import GenerateQuote

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        # THIS SHOULDNT BE HARD CODED FOR PROJECT

        # sets the first persons quote to equal to equal the GenerateQuote class in the library
        person1 = GenerateQuote()

        # get the info from inputs using the GET
        if self.request.GET:
            person1.vehicle_type = self.request.GET['Veh_Type']
            person1.recent_incident = self.request.GET['Rec_Incident']
            person1.car_value = self.request.GET['Car_Val']
            person1.coverage_amount = self.request.GET['Cov_Amount']
            # display info to the page using WRITE
            # some of this had to be split up for proper display
            self.response.write(p.head + p.body2 + person1.vehicle_type + p.body3 + person1.recent_incident + p.body4 + person1.car_value + p.body5 + person1.coverage_amount + p.body6)
            self.response.write(person1.total_coverage)
            self.response.write(p.body7)
            self.response.write(person1.monthly_cost)
            print person1.coverage_amount
        else:
            # else if there is no request it will just display
            self.response.write(p.print_out())

        #self.response.write(person1.car_value)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
