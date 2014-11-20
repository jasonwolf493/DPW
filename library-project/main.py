'''
Jason Wolf
11/5/2014
DPW
Python 2
'''
import webapp2


from pages import Page, FormPage, FourZeroFourPage, ContactPage
from library import GeneratePage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #page for class
        try:
            if self.request.GET['link'] == 'form':
                p = FormPage()
            elif self.request.GET['link'] == 'index':
                p = Page()
            elif self.request.GET['link'] == 'contact':
                p = ContactPage()
            else:
                p = FourZeroFourPage()
        except:
            p = Page()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        # THIS SHOULDNT BE HARD CODED FOR PROJECT
        page_gen = GeneratePage()
        #person1.vehicle_type = "Truck"
        if self.request.GET:
            page_gen.link = self.request.GET['link']
            #person1.recent_incident = self.request.GET['Rec_Incident']
            #person1.car_value = self.request.GET['Car_Val']
            #person1.coverage_amount = self.request.GET['Cov_Amount']
            #self.response.write(p.head + p.body2 + page_gen.link + p.body3 + page_gen.recent_incident + p.body4 + page_gen.car_value + p.body5 + page_gen.coverage_amount + p.body6)
            self.response.write(p.print_out())

        else:
            self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
