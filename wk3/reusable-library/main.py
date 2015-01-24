#import the different python documents
from Pages import FormPage, ResultsPage
from library import Paycheck, Calculate
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #set cal as an instance of calculate
        cal = Calculate()
        #set pc1 to equal the paycheck function
        pc1 = Paycheck()
        #set some default values for paycheck
        pc1.biweekly = False
        pc1.wage = 10
        pc1.hours = 40
        pc1.holiday = 1

        #if we get a GET request then set the correct values and show the results page
        if self.request.GET:
            pc1.wage = self.request.GET['wage']
            pc1.hours = self.request.GET['hours']
            pc1.holiday = self.request.GET['holiday']
            pc1.biweekly = self.request.GET['biweekly']
            p = ResultsPage()
            p.body += cal.summary_text(pc1)
        #else lets continue showing the formpage
        else:
            p = FormPage()

        #write to the page using the printout function
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
