class DataObject(object):
    def __init__(self):
        #this is the data we will need for the about page.
        self.__about = """
        <h1>About Us</h1>
        <img id="index1" alt="A professional grooming a dog." src="/imgs/about.jpg" height="253px" width="380px">
        <p id="info">Learn more about us!</p>
        <p>We've been working with pets for years, we provide professional services from professional staff and affordable prices. We offer cuts, coat cleaning, conditioning, and some flea and tick programs. We also make the service customizable, so your pet can get the best experience. You can select shampoos and conditioners you like along with other products you find best suitable for your pet.</p>
        """
        #some more data, we will use this for the contact page.
        self.__contact = """
        <h1>Contact Us</h1>
        <img id="index1" alt="friendly receptionist" src="/imgs/contact.jpg" height="253px" width="380px">
        <p id="info">Get in contact with us!</p>
        <div>
            <p>Here is our contact info, just for you!</p>
            <p>Phone Number: 1-123-1234</p>
            <p>Email: Petcuts@petcuts.com</p>
            <p>Address: 123 Main St.</p>
        </div>
        """
        #this is for the home page.
        self.__index = """
        <h1>Pet Cuts</h1>
        <img id="index1" alt="Dog getting fur cut under chin." src="/imgs/index1.jpg" height="253px" width="380px">
        <p id="info">Premium grooming for your pet!<p>
        <p>We offer the best grooming services you can find for your pet. Our experienced pet dressers will give your pet the greatest experience possible. Our site provides you with a way to find out more info about us. But if you dont see what you are looking for just get in touch with us and we'll help you out.</p>

        """
        #And... the animal page
        self.__animals = """
        <h1>Animals</h1>
        <img id="index1" alt="A dog and cat." src="/imgs/animals.jpg" height="335px" width="380px">
        <p id="info">Who do we provide services to?<p>
        <p>The pets that we provide services for are:</p>
        <ul>
            <li>Dogs</li>
            <li>Cats</li>
            <li>Birds*</li>
        </ul>
        <p>Not all of our services are available for all pets, if you dont see your pet or have other questions <a id="textlink" href="?page=contact">contact us</a> today.</p>
        """
        #services page
        self.__services = """
        <h1>Services</h1>
        <img id="index1" alt="A dog bath" src="/imgs/services.jpg" height="252px" width="380px">
        <p id="info">Check out some of the services we provide.<p>
        <p>Some of the services we provide are:</p>
        <ul>
            <li>Cutting</li>
            <li>Washing</li>
            <li>Conditioning</li>
            <li>Anti flea and tick services</li>
            <li>Wing clippings for birds</li>
        </ul>
        <p>Is there a service you want that you don't see? Let us know! We built this company for you and your pets!</p>
        """
        #and the different cuts the company offers
        self.__cuts = """
        <h1>Cuts</h1>
        <img id="index1" alt="A dog and cat." src="/imgs/cuts.jpg" height="380px" width="253px">
        <p id="info">These are some of the cut we do.<p>
        <p>Cuts we provide:</p>
        <ul>
            <li>The Schnauzer Cut</li>
            <li>Cocker Cut</li>
            <li>Poodle Cut</li>
            <li>Lamb Cut</li>
            <li>Lion Cut</li>
            <li>The Teddy Bear Cut</li>
            <li>All Over</li>
            <li>Poodle Face</li>
            <li>Topknot</li>
            <li>Lion Cut</li>
        </ul>
        <p>This is just to name a few for the full catalog come to the salon we'll be happy to show you.</p>
        """
#now once this is called...
    def page_return(self):
        #check what page the user is trying to see
        if self.page == "index":
            #if its the index lets pass them the index data.... And so on...
            return self.__index
        elif self.page == "about":
            return self.__about
        elif self.page == "animals":
            return self.__animals
        elif self.page == "services":
            return self.__services
        elif self.page == "cuts":
            return self.__cuts
        elif self.page == "contact":
            return self.__contact
        #But if we get some unrecognized response, lets play it safe and give them the index page
        else:
            return self.__index

        #getters and setters.... So we can set __page and get page.
        @property
        def page(self):
            return self.__page

        @page.setter
        def page(self, y):
            self.__page = y