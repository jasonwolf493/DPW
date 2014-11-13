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

        person1 = GenerateQuote()
        #person1.vehicle_type = "Truck"
        if self.request.GET:
            person1.vehicle_type = self.request.GET['Veh_Type']

            person1.recent_incident = self.request.GET['Rec_Incident']
        #person1.recent_incident = "Yes"
        #person1.car_value = 5000
            person1.car_value = self.request.GET['Car_Val']
        #person1.coverage_amount = 1000
            self.response.write(p.print_completion())

        else:
            self.response.write(p.print_out())

        #self.response.write(person1.car_value)
'''
        print(person1.car_value)
        print(person1.coverage_amount)
        print(person1.total_coverage)
        print(person1.recent_incident)
        print(person1.vehicle_type)
        print(person1.car_type_risk)
        print(person1.monthly_cost)
'''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
