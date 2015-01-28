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
        <p>Anything for the body will go here</p>
        """
        self.__error = ""
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.__error + self.close
        return all
