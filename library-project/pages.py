"""
Jason Wolf
11/5/2014
DPW
Python 2
"""

#this is just the page for the html of the page nothing more!
class Page(object):
    def __init__(self):
        self.title = "Free Online Auto Quote!"
        self.css = "css/main.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Free Online Auto Quote!</title>
        <link href="css/main.css" rel="stylesheet" type="text/css">

    </head>
    <body>
        """

        self.body = """
        <div class=container>
            <a href="?link=index">Home</a><a href="?link=form">Sign Up</a><a href="?link=contact">Contact Us</a>
        """

        self.error = ''
        self.close = """
        </div>

    </body>
</html>
        """
        # below we def print_out which will just return the html

    def print_out(self):
        all = self.head + self.body + self.error + self.close
        return all


class FormPage(Page):
    def __init__(self):
        # constructor for the super class
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        # first name last name button

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr

        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item add it otherwise end tag
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'
        print self._form_inputs

        # polymorphism here
    def print_out(self):
        return self.head + self.body + self._form_open + self._form_inputs + self._form_close + self.close


class FourZeroFourPage(Page):
    def __init__(self):
        super(FourZeroFourPage, self).__init__()
        self._error = '''
            <h1>404 Page Not Found</h1>
            <p>The link you have followed has lead you to a page that no longer exists, or never did.</p><br>
            <p>Sorry for the inconvenience...</p>

        '''
    def print_out(self):
        all = self.head + self.body + self._error + self.close
        return all


class ContactPage(Page):
    def __init__(self):
        super(ContactPage, self).__init__()
        self._contact = '''
            <h1>Did you need something?</h1>
            <p>If so, here's our contact info feel free to use it!</p><br>
            <p>Phone: 1-555-555-5555</p><br>
            <p>Email: FakeEmail@Fake.com</p><br>
            <p>Address: 1234 placeholder blv. USA

        '''
    def print_out(self):
        all = self.head + self.body + self._contact + self.close
        return all


'''

                   <form method="GET">
                <h1>Fill Out Your Free Quote</h1>
                <input id="input_box" type="number" placeholder="Car Value:" name="Car_Val"><br>
                <input id="input_box" type="number" placeholder="Coverage:" name="Cov_Amount"><br>
                <h2>Vehicle Type:</h2>
                <select class="drop_down" name="Veh_Type">
                    <option value="Truck">Truck</option>
                    <option value="Sports Car">Sports Car</option>
                    <option value="Economy">Economy Car</option>
                    <option value="Other">Other</option>
                </select>
                <h2>Recent Incident:</h2>
                <p class="info">In the last 12 months.<p>
                <select class="drop_down" name="Rec_Incident">
                    <option value="Yes">Yes</option>
                    <option value="No">No</option>
                </select><br>
                <button class="submit" type="submit" value="Submit">Submit</button>
            </form>


'''