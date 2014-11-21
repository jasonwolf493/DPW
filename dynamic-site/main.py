'''
Jason Wolf
11/19/2014
DPW
Dynamic Page
'''
import webapp2

# import all the required parts for the main handler
from pages import Page, FormPage, FourZeroFourPage, ContactPage, IndexPage
from library import GenerateInputs, GenerateContacts, GenerateSales

# the main handler, it does just that... handles everything
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # try/except with a nested if statement that checks the link attribute then sets p to the correct data object in pages
        try:
            if self.request.GET['link'] == 'form':
                p = FormPage()
            elif self.request.GET['link'] == 'index':
                p = IndexPage()
            elif self.request.GET['link'] == 'contact':
                p = ContactPage()
            else:
                p = FourZeroFourPage()
        except:
            p = Page()

        # sets the correct array for the correct page
        p.inputs = GenerateInputs.inputs
        p.contacts = GenerateContacts.inputs
        p.sales = GenerateSales.inputs


        # writes everything to the page
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
