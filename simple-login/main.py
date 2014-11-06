'''
name: Jason Wolf
date: 11/5/2014
class: DPW
assignment: Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Login</title>
    </head>
    <body>'''

        page_body = '''<form method="GET">
            <label>Name:</label><input type="text" name="user"/>
            <label>Email:</label><input type="text" name="email"/>
            <input type="submit" value="Submit" />'''
        page_close = '''</form>
    </body>
</html>
        '''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
        else:
            self.response.write(page_head + page_body + page_close) #this prints info
        #code goes here


#never touch!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
