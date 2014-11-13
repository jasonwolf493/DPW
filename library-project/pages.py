"""
Jason Wolf
11/5/2014
DPW
Python 2
"""

#this is just the page for the html of the page nothing more!
class Page(object):
    def __init__(self):
        self.__title = "Free Online Auto Quote!"
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

        </div>



        """
        self.body2 = """
        <div class=container>
            
        </div>



        """

        self.__error = ''
        self.__close = """
    </body>
</html>
        """
        # below we def print_out which will just return the html
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all

        # display HTML after form completion
    def print_completion(self):
        complete = self.__head + self.body2 +  self.__error + self.__close
        return complete