'''
Jason Wolf
11/19/2014
DPW
Dynamic Page
'''
import webapp2


from pages import Page, FormPage, FourZeroFourPage, ContactPage, IndexPage
from library import GeneratePage, GenerateInputs, GenerateContacts, GenerateSales


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #page for class
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
        page_gen = GeneratePage()

        p.inputs = GenerateInputs.inputs
        p.contacts = GenerateContacts.inputs
        p.sales = GenerateSales.inputs

        if self.request.GET:
            page_gen.link = self.request.GET['link']
            self.response.write(p.print_out())

        else:
            self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
