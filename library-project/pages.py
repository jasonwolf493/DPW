"""
Jason Wolf
11/5/2014
DPW
Python 2
"""

#this is just the page for the html of the page nothing more!
class Page(object):
    def __init__(self):
        # this is the title of the page and will show up in the tab
        self.title = "Free Online Auto Quote!"
        # this is the link to the css file
        self.css = "css/main.css"
        # this is the head of the page and it has all the required links and opening tags
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Free Online Auto Quote!</title>
        <link href="css/main.css" rel="stylesheet" type="text/css">

    </head>
    <body>
        """
        # this is the actual body of the document anything that is typed in here will show up in the body
        self.body = """
        <div class=container>
            <form method="GET">
                <h1>Fill Out Your Free Quote</h1>
                <input id="input_box" type="number" placeholder="Car Value:" name="Car_Val"><br>
                <input id="input_box" type="number" placeholder="Coverage:" name="Cov_Amount"><br>
                <h2>Vehicle Type:</h2>
                <select class="drop_down" name="Veh_Type">
                    <option value="Truck">Truck</option>
                    <option value="Sports Car">Sports Car</option>
                    <option value="Economy">Economy Car</option>
                    <option value="Other">Other</option>
                </select>
                <h2>Recent Incident:</h2>
                <p class="info">In the last 12 months.<p>
                <select class="drop_down" name="Rec_Incident">
                    <option value="Yes">Yes</option>
                    <option value="No">No</option>
                </select><br>
                <button class="submit" type="submit" value="Submit">Submit</button>
            </form>





        """

        # These are additional body"parts" that will show up in the body if needed
        self.body2 = """
        <div class=container>
        <h1>Personalized Auto Quote</h1>
        <p>Vehicle Type:</p> """
        self.body3 = """
        </br><p>Recent Incident:</p> """
        self.body4 = """
        </br><p>Vehicle Value:</p>
        """
        self.body5 = """
        </br><p>Coverage:</p>
        """
        self.body6 = """
        </br><p>Total Coverage:</p>
        """
        self.body7 = """
        </br><p class="Monthly">Monthly Payment:</p>
        """
        self.error = ''
        self.close = """
        </div>

    </body>
</html>
        """
        # below we def print_out which will just return the html
    def print_out(self):
        # concats most the above info
        all = self.head + self.body + self.error + self.close
        return all

        # display HTML after form completion
    def print_completion(self):
        # display info after the form is complete
        complete = self.head + self.body2 + self.body3 + self.error + self.close
        return complete