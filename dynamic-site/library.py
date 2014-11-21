__author__ = 'Jason'

# edit info on pages with the arrays below


class GeneratePage(object):  # this has every attribute we'll need
    def __init__(self):
        # link allows the classes to go to the correct page
        self.link = ""

# this array provides the attributes for the form section
class GenerateInputs(object):
    inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['email', 'email', 'Email'], ['Submit', 'submit']]

# this array holds all of the contact info for the contact page
class GenerateContacts(object):
    inputs = ['Phone: ', '1-555-555-5555', 'Email: ', 'FakeEmail@Fake.com', 'Address: ', '1234 placeholder blv. USA']

# lastly this array holds the data for the sales on the index page.
class GenerateSales(object):
    inputs = ['Sales for anyone: ', '<li>Purchase a new tractor blade in the next 24 hours and get one 50% off!', '<li>Become a member and get 20% off your first month.<br>', '<br>Exclusive sales for members: ', '<li>Spend $100 and get a $50 gift card', '<li>Invite someone to become a member and get next months membership FREE! ', '<li>Schedule your winterization this week and get $12 off.']