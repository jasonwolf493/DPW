#this is the super class for the html, we will use this as the "Template"
class Page(object):
    def __init__(self):
        self.__title = "PageTitle"
        self.css = "css/styles.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = """
        <div id="navContainer">
            <a id="navtext" href="?page=index">Home</a>
            <a id="navtext" href="?page=about">About</a>
            <a id="navtext" href="?page=contact">Contact Us</a>
            <a id="navtext" href="?page=animals">Animals</a>
            <a id="navtext" href="?page=services">Services</a>
            <a id="navtext" href="?page=cuts">Cuts</a>
        </div>
        <div id="container">
        """
        self._error = ""
        self.close = """
        </div>
    </body>
</html>
        """
    #this is the super's print out function, we will override this in the sub class.
    def print_out(self, p):
        #return some basic data
        return self.head + self.body + self.close


#this is now a sub class to Page()
class OtherPage(Page):
    def __init__(self):
        #we have to call the super's init func here
        super(OtherPage, self).__init__()
        #we will use _content to store content that needs to be displayed to the page
        self._content = ""
    #this is essentially like the old print out function but a little more robust

    def print_out(self, p):
        #we set our _content to the data the we have passed to this function
        self._content = p
        #we are going to set 'all' to equal most of the things from our super class...
        #but we are going to use our _content var that we made as well, This holds...
        #exclusive content that our super class doesnt have
        all = self.head + self.body + self._content + self._error + self.close
        #finally lets return all that! So main can display it.
        return all