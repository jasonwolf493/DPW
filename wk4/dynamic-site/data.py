class DataObject(object):
    def __init__(self):
        #default values if there are no inputs
        self.__about = """
        <h1>About Us</h1>
        <p id="info">Learn more about us!</p>
        <p>We've been working with pets for years, we provide professional services from professional staff and affordable prices. We offer cuts, coat cleaning, conditioning, and some flea and tick programs. We also make the service customizable, so your pet can get the best experience. You can select shampoos and conditioners you like along with other products you find best suitable for your pet.</p>
        """
        self.__contact = """
        <h1>Contact Us</h1>
        <p id="info">Get in contact with us!</p>
        <div>
            <p>Here is our contact info, just for you!</p>
            <p>Phone Number: 1-123-1234</p>
            <p>Email: Petcuts@petcuts.com</p>
            <p>Address: 123 Main St.</p>
        </div>
        """
        self.__index = """
        <h1>Pet Cuts</h1>
        <img id="index1" alt="Dog getting fur cut under chin." src="/imgs/index1.jpg">
        <p id="info">Premium grooming for your pet!<p>
        <p>We offer the best grooming services you can find for your pet. Our experienced pet dressers will give your pet the greatest experience possible. Our site provides you with a way to find out more info about us. But if you dont see what you are looking for just get in touch with us and we'll help you out.</p>

        """
        self.__animals = """
        <h1>Animals</h1>
        <p id="info">Who do we provide services to?<p>
        <p>The pets that we provide services for are:</p>
        <ul>
            <li>Dogs</li>
            <li>Cats</li>
            <li>Birds*</li>
        </ul>
        <p>Not all of our services are available for all pets, if you dont see your pet or have other questions <a href="contact">contact us</a> today.</p>
        """
        self.__services = """
        <h1>Services</h1>
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
        self.__cuts = """
        <h1>Cuts</h1>
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

    def page_return(self):
        if self.page == "index":
            return self.__index
            #return self.index
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
        else:
            return self.__index

        #getters and setters
        @property
        def page(self):
            return self.__page

        @page.setter
        def page(self, y):
            self.__page = y