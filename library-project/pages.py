"""
Jason Wolf
11/5/2014
DPW
Python 2
"""

#this is just the page for the html of the page nothing more!
class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/main.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css">
    </head>
    <body>
        """

        self.body = "Welcome to the page"
        self.__error = ''
        self.__close = """
    </body>
</html>
        """
        # below we def print_out which will just return the html
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all