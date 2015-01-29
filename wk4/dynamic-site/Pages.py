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
            <a id="navtext" href="?page=index">Home</a><a id="navtext" href="?page=about">About</a><a id="navtext" href="?page=contact">Contact Us</a><a id="navtext" href="?page=animals">Animals</a><a id="navtext" href="?page=services">Services</a><a id="navtext" href="?page=cuts">Cuts</a>
        </div>
        <div id="container">

        """
        self._error = ""
        self.close = """
        </div>
    </body>
</html>
        """


class OtherPage(Page):
    def __init__(self):
        super(OtherPage, self).__init__()
        self._content = ""

    def content_print(self, p):
        self._content = p
        all = self.head + self.body + p + self._error + self.close
        return all