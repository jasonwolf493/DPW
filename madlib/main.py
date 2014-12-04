"""
Jason Wolf
11/5/2014
DPW
Data-Objects
"""
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        char1 = Character()
        char1.name = "Jack"
        char1.profession = "peasant"
        char1.race = "elf"
        char1.age = 19 * 1.5

        char2 = Character()
        char2.name = "John"
        char2.profession = "miner"
        char2.race = "dwarf"
        char2.age = 53 / 2

        char3 = Character()
        char3.name = "Jason"
        char3.profession = "peddler"
        char3.race = "human"
        char3.age = 21

        chars = [char1, char2, char3]
        x = 0
        for people in chars:
            self.response.write(Character.gen_story(people, x))
            x += 1
            print people.name



class Character(object):
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""
        self.race = ""
        print self.name

    def gen_story(self, x):

        text = self.name + " he has spent most of his life as a " + self.profession + ", he is " + str(self.age) + "yrs old in human years and he is a " + self.race
        if self.race == "elf":
            text = text + " making him " + str(self.age / 1.5)
        elif self.race == "dwarf":
            text = text + " making him " + str(self.age * 2)

        if x == 0:
            text = "The journey begins with three brave souls, " + text
            return text + ". "
        else:
            return text + ". "




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
