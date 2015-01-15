import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Shippr</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div id="container">
        """

        self.body = """
            <h1>Shippr</h1>
            Fill your shipping info below and shippr will handle the rest!
        """
        self.form = """
            <form method="GET" action="">
                <input id="textinput" type="text" placeholder="John" name="first_name" required/>
                <input id="textinput" type="text" placeholder="Doe" name="last_name" required/><br>
                <input id="addressinput" type="text" placeholder="123 Main St." name="address" required/>
                <br>
                <select name="state">
                    <option value="Connecticut">Connecticut</option>
                    <option value="Massachusetts">Massachusetts</option>
                    <option value="Ohio">Ohio</option>
                    <option value="Pennsylvania">Pennsylvania</option>
                </select>
                <br><input id="radio" type="radio" name="agree" value="true">I agreed to the shipping terms and conditions.
                <br><input id="submit" type="submit" value="Submit" />
            </form>
        """
        self.close = """
        </div>
    </body>
</html>
        """

        if self.request.GET:
            first_name = self.request.GET['first_name']
            last_name = self.request.GET['last_name']
            address = self.request.GET['address']
            state = self.request.GET['state']
            self.body = "<h1>Thanks!</h1><h2>" + first_name + " " + last_name + " our team will jump right on it.</h2>"
            self.response.write(self.head + self.body + " <br>First Name: " + first_name + "<br>Last Name: " + last_name + "<br>Address: " + address + "<br>State: " + state + "<br><br>Your package will leave our facility momentarily <br>" + "<a href='/'>Ship something else!</a>" + self.close)
        else:
            self.response.write(self.head + self.body + self.form + self.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
