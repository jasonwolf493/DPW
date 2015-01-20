from Pages import FormPage, ResultsPage
from library import Paycheck, Calculate
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        cal = Calculate()
    #Paycheck calculator
        pc1 = Paycheck()
        pc1.biweekly = False
        pc1.wage = 10
        pc1.hours = 40
        pc1.holiday = 1

        if self.request.GET:
            pc1.wage = self.request.GET['wage']
            pc1.hours = self.request.GET['hours']
            pc1.holiday = self.request.GET['holiday']
            pc1.biweekly = self.request.GET['biweekly']
            p = ResultsPage()
            p.body += cal.summary_text(pc1)
        else:
            p = FormPage()

       # p.body += cal.summary_text(pc1)
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
