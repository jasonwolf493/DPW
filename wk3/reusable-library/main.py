from Pages import FormPage
from library import Paycheck
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        self.response.write(p.print_out())

    #Paycheck calculator
        #biweekly?
        #Hourly pay
        #hours worked
        #holiday hours

        #fix this hard code make it user input
        pc1 = Paycheck()
        pc1.biweekly = True
        pc1.wage = 10
        pc1.hours = 40
        pc1.holiday = 0


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
