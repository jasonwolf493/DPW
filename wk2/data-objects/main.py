
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "tattooine"

        leia = Character()
        leia.name = "Princess leia"
        leia.profession = "princess"
        leia.age = luke.age
        luke.home_planet = "Alderan"



class Character(object):
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
