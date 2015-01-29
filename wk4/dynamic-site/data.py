class DataObject(object):
    def __init__(self):
        #default values if there are no inputs
        self.__about = """
        <h1>About Us</h1>
        <p>Learn more about us!</p>
        """
        self.__contact = """
        <h1>Contact Us</h1>
        <p>Get in contact with us!</p>
        """
        self.__index = """
        <h1>Welcome to the page</h1>
        <p>Here is some more text for the index page<p>
        """
        self.__four = ""
        self.__five = ""
        self.__page = ""

    def page_return(self):
        if self.page == "index":
            return self.__index
            #return self.index
        elif self.page == "about":
            return self.__about
        elif self.page == "contact":
            return self.__contact
        else:
            pass
            #return self.index

        #getters and setters
        @property
        def page(self):
            return self.__page

        @page.setter
        def page(self, y):
            self.__page = y