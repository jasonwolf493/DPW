"""
Jason Wolf
11/5/2014
DPW
Python 2
"""

#this is just the page for the html of the page nothing more!
class Page(object):
    def __init__(self):
        self.title = "Free Online Auto Quote!"
        self.css = "css/main.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Free Online Auto Quote!</title>
        <link href="css/main.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        """

        self.body = """
        <div class=container>
            <form method="GET">
                <input type="number" placeholder="Car Value:" name="Car_Val"><br>
                <input type="number" placeholder="Coverage:" name="Cov_Amount"><br>
                <select name="Veh_Type">
                    <option value="Truck">Truck</option>
                    <option value="Sports Car">Sports Car</option>
                    <option value="Economy">Economy Car</option>
                    <option value="Other">Other</option>
                </select>
                <select name="Rec_Incident">
                    <option value="Yes">Yes</option>
                    <option value="No">No</option>
                </select>
                <input class="submit" type="submit" value="Submit" />
            </form>





        """
        self.body2 = """
        <div class=container>
        <h1>Your Auto Quote</h1>
        Vehicle Type: """
        self.body3 = """
        </br>Recent Incident: """
        self.body4 = """
        </br>Vehicle Value:
        """
        self.body5 = """
        </br>Coverage:
        """
        self.body6 = """
        </br>Total Coverage:
        """
        self.body7 = """
        </br>Monthly Payment:
        """
        self.error = ''
        self.close = """
        </div>
    </body>
</html>
        """
        # below we def print_out which will just return the html
    def print_out(self):
        all = self.head + self.body + self.error + self.close
        return all

        # display HTML after form completion
    def print_completion(self):
        complete = self.head + self.body2 + self.body3 + self.error + self.close
        return complete