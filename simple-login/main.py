'''
name: Jason Wolf
date: 11/5/2014
class: DPW
assignment: Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(self):
        pass
        #code goes here


#never touch!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
