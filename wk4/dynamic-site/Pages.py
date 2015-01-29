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
        <div id="container">
        <div id="navContainer">
            <a href="?page=index">Home</a><a href="?page=about">About</a><a href="?page=contact">Contact Us</a>
        </div>
        """
        self.__error = ""
        self.close = """
        </div>
    </body>
</html>
        """

    def print_out(self, p):
        all = self.head + self.body + "This is from PAGES>>>" + p + "<<<" + self.__error + self.close
        return all

