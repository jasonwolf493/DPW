"""
Jason Wolf
11/5/2014
DPW
Python 2
"""
class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/main.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css">
    </head>
    <body>
        """

        self.body = "Welcome to the page"
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all