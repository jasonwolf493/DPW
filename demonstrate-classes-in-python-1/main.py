'''
Jason Wolf
11/5/2014
DPW
Demonstrate python1
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "about us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "contact us"
        about_button.show_label()



class Button(object):
    def __init__(self):
        print"Contructor method ran"
        self.label = "" #public attribute
        self.__size = 60 #private attribute
        self._color = "0x00000" # _ protected attribute
       # self.on_roll_over("here is the message!")

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button." + message

    def show_label(self):
        print "My label is " + self.label




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
