class FormPage(object):
    def __init__(self):
        #here is the title of the document
        self.__title = "Welcome!"
        #this is the link to the css
        self.css = "css/styles.css"
        #here is everything that will be included in the head
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        #now here's everything for the body
        self.body = """<div id="formdiv">
Paycheck Calculator
        <form method="GET" action="" name="form" onsubmit="return validateForm();">
            <input id="wage" type="number" placeholder="Hourly Wage:" name="wage" required/><br>
            <input id="textinput" type="number" placeholder="Hours:" name="hours" required/><br>
            <input id="holiday" type="number" placeholder="Holiday Hours:" name="holiday" required/>
            <br>Bi-Weekly?<br>
            <div id="radio1">
            Yes:<input id="radio" type="radio" name="biweekly" value="True" /><br>
            </div>
            <div id="radio2">
            No:<input id="radio" type="radio" name="biweekly" value="False" checked="checked" />
            </div>
            <br><input id="submit" type="submit" value="Submit" onclick="validateForm()" />
        </form>
        </div>

                    """
        #if we have any errors they go here
        self.__error = ''
        #now this closes all of the opened tags
        self.__close = """
        <script src="/js/main.js"></script>
    </body>
</html>
        """
    #this is the printout function we will call this to write some html to the page
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all


class ResultsPage(object):
    def __init__(self):
        #and this is the title
        self.__title = "Welcome!"
        #this is the css to the doc
        self.css = "css/styles.css"
        #this is the head of the document
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Here's Your Results:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
        """
        #this is the body of the document
        self.body = "<div id='formdiv'><h3>Weekly Income*</h3><br>"
        #this spot is for errors
        self.__error = ''
        #here we close all of the open tags
        self.__close = """
                <p id="info">The dollar amount of your check was determined before taxes, union fees, or any other type withholding.</p>
            </div>
        <script src="/js/main.js"></script>
    </body>
</html>
        """
    #the alternative printout for after the form has been completed
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all

