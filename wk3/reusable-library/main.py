from Pages import FormPage, ResultsPage
from library import Paycheck, Calculate
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:
            p = ResultsPage()
        else:
            p = FormPage()
        cal = Calculate()


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
        pc1.holiday = 1
        #cal.total_up(pc1)
        #self.response.write(cal.summary_text(pc1))

        p.body = cal.summary_text(pc1)
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
