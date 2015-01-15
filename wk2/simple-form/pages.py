class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = "Welcome to my python page"
        self.close = """
    </body>
</html>
        """

    def build_page(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all