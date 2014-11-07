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
        <link href="css/main.css" rel="stylesheet" type="text/css">
    </head>
    <body>'''


        #<label>First Name:</label>
        #<label>Last Name:</label>
        #<label>Address:</label>
        page_shipped = '''
        <div class="title">
            <h1>Christmas Shipper</h1>
        </div>
        <div class="info">

        '''
        page_body = '''
        <div class="title">
            <h1>Christmas Shipper</h1>
        </div>
        <div class="center">
        <form method="GET">
            <input type="text" placeholder="First Name" name="first"/><br>
            <input type="text" placeholder="Last Name" name="last"/><br>
            <input class="address" type="text" placeholder="Address" name="address"/><br>
            <label>Shipping:</label><br>
            <select name="shipping">
                <option value="ground shipping">Ground</option>
                <option value="two day shipping">2 Day</option>
                <option value="overnight shipping">Overnight</option>
            </select>
            <input class="submit" type="submit" value="Submit" />'''
        page_close = '''</form></div>
    </body>
</html>
        '''
        if self.request.GET:
            first_name = self.request.GET['first']
            last_name = self.request.GET['last']
            address = self.request.GET['address']
            shipping = self.request.GET['shipping']
            if shipping == "ground shipping":
                days = "5"
            if shipping == "two day shipping":
                days = "2"
            else:
                days = "1"



            self.response.write(page_head + page_shipped + first_name + " " + last_name + "'s package will arrive at " + address + " via " + shipping + " about " + days + " day after the package departs."  + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #this prints info
        #code goes here


#never touch!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
