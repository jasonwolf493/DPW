"""
Jason Wolf
11/19/2014
DPW
Dynamic page
"""
from library import GenerateInputs
#This Is the basic page guidelines


class Page(object):
    def __init__(self):
        self.css = "css/main.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple server side template</title>
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


class IndexPage(Page):
    def __init__(self):
        # constructor for the super class
        super(IndexPage, self).__init__()
        self.__inputs = []
        self._sales_text = ''
        self.__sales = []
        self._index_body = '''
            <h1>Welcome!</h1>
            <p class="info">Check out our sales below!</p>
            <p class="info">Some of these sales are exclusive to members.<p>
            <h2>Today's Sales</h2>

            '''
        # first name last name button

    @property
    def sales(self):
        pass

    @sales.setter
    def sales(self, arr):
        self.__sales = arr
        for item in arr:
            self._sales_text += '' + str(item) + ''
            #if there is a third item add it otherwise end tag

        print self._sales_text
        # polymorphism here
    def print_out(self):
        return self.head + self.body + self._index_body + self._sales_text + self.close


class FormPage(Page):
    def __init__(self):
        # constructor for the super class
        super(FormPage, self).__init__()
        self._form_open = '<form class="input_box" method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        self._text = '<p>Keep in mind the submit button breaks I could fix with JQuery by appending the missing "Link" attribute to the url</p>'
        self._form_body = '''
            <h1>Sign up</h1>
            <p class="info">Interested in receiving updates?<br></p>
            <p class="info">Use this form to get emails.<p>

            '''
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
                self._form_inputs += '" placeholder="' + item[2] + '" /><br>'
            except:
                self._form_inputs += '" />'
        print self._form_inputs

        # polymorphism here
    def print_out(self):
        return self.head + self.body + self._form_body + self._text + self._form_open + self._form_inputs + self._form_close + self.close


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

        self._add_contact = '''
            <h1>Did you need something?</h1>
            <p class="info">If so, here's our contact info feel free to use it!</p><br>'''
    @property
    def contacts(self):
        pass

    @contacts.setter
    def contacts(self, con):
        self._contact = con
        for item in con:
            self._add_contact += '<p>' + str(item) + ''
            #if there is a third item add it otherwise end tag

        print self._add_contact

        # polymorphism here


    def print_out(self):
        all = self.head + self.body + self._add_contact + self.close
        return all
