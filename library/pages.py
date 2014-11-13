"""
Jason Wolf
11/5/2014
DPW
Python 2
"""
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
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all