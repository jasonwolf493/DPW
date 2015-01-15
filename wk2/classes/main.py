
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        contact_button = Button()
        about_button.click()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button.label = "contact us"
        contact_button.show_label()


class Button(object):
    def __init__(self):
        print " constructor method ran"
        self.label = ""
        self.click()
        self.on_roll_over("Hello!")

    def click(self):
        print "ive been clicked"

    def on_roll_over(self, message):
        print "rolled over" + message

    def show_label(self):
        print "my label is " + self.label


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
