class FormPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = """
FORM PAGE
        <form method="GET" action="" name="form" onsubmit="return validateForm();">
            <input id="wage" type="number" placeholder="Hourly Wage:" name="wage" required/><br>
            <input id="textinput" type="number" placeholder="Hours:" name="hours" required/><br>
            <input id="textinput" type="number" placeholder="Holiday Hours:" name="holiday" required/>
            <br>Bi-Weekly?<br>
            Yes:<input id="radio" type="radio" name="biweekly" value="True" /><br>
            No:<input id="radio" type="radio" name="biweekly" value="False" checked="checked" />
            <br><input id="submit" type="submit" value="Submit" onclick="validateForm()" />
        </form>

                    """
        self.__error = ''
        self.__close = """
        <script src="/js/main.js"></script>
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all


class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Here's Your Results:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
        """

        self.body = "RESULTS PAGE<br>"
        self.__error = ''
        self.__close = """
        <script src="/js/main.js"></script>
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all

