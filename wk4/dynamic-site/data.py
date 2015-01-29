class DataObject(object):
    def __init__(self):
        #default values if there are no inputs
        self.__about = ""
        self.__contact = ""
        self.index = "some more text from index"
        self.__four = ""
        self.__five = ""
        self.__page = ""

    def page_return(self):
        if self.page == "index":
            return self.page + self.index
            #return self.index
        elif self.page == "about":
            return self.page
        elif self.page == "contact":
            return self.page
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