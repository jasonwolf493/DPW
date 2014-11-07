'''
name: Jason Wolf
date: 11/5/2014
class: DPW
assignment: Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything

        #this is the head of the html doc it contains the title and link to CSS
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Christmas Shipper</title>
        <link href="css/main.css" rel="stylesheet" type="text/css">
    </head>
    <body>'''


        #<label>First Name:</label>
        #<label>Last Name:</label>
        #<label>Address:</label>

        #this portion of HTML will only be showed once the user has submitted their info
        page_shipped = '''
        <div class="title">
            <h1>Christmas Shipper</h1>
        </div>
        <div class="info">

        '''
        #the body below contains all the main HTML you see when you first look at the page
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
        #this just makes sure that the div, form, body, and html its self is closed
        page_close = '''</form></div>
    </body>
</html>
        '''
        #requests info from the client so we can build our vars
        if self.request.GET:
            first_name = self.request.GET['first']
            last_name = self.request.GET['last']
            address = self.request.GET['address']
            shipping = self.request.GET['shipping']
            #this is to set the days var to make sure it corresponds with the selected shipping method above, we will use the days var later.
            if shipping == "ground shipping":
                days = "5"
            if shipping == "two day shipping":
                days = "2"
            #if they didnt select ground or two day shipping they obviously selected overnight
            else:
                days = "1"

            #so now that we got our vars made thanks to the client info we are just going to write it, we also use the page_shipped var we made above to display. and we dont use the page_body
            self.response.write(page_head + page_shipped + first_name + " " + last_name + "'s package will arrive at " + address + " via " + shipping + " about " + days + " day after the package departs."  + page_close)
        #but if there is no request we'll just make sure all the forms are displayed for the user
        else:
            self.response.write(page_head + page_body + page_close) #this prints info



#never touch!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
