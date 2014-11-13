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
        person1.vehicle_type = self.request.GET['Veh_Type']
        person1.recent_incident = self.request.GET['Rec_Incident']
        #person1.recent_incident = "Yes"
        person1.car_value = 5000
        person1.coverage_amount = 1000
        print("Value: " + str(person1.car_value))
        print("Coverage amount: " + str(person1.coverage_amount))
        print("Total Coverage: " + str(person1.total_coverage))
        print("Recent Driving Incident: " + str(person1.recent_incident))
        print("Car Type: " + str(person1.vehicle_type))
        print("Risk: " + str(person1.car_type_risk))
        print("Monthly Cost: " + str(person1.monthly_cost))

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
