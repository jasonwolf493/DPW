__author__ = 'Jason'

# Fill in the contact info with some info here


class GeneratePage(object):  # this has every attribute we'll need
    def __init__(self):
        self.link = ""


class GenerateInputs(object):
    inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['email', 'email', 'Email'], ['Submit', 'submit']]


class GenerateContacts(object):
    inputs = ['Phone: ', '1-555-555-5555', 'Email: ', 'FakeEmail@Fake.com', 'Address: ', '1234 placeholder blv. USA']


class GenerateSales(object):
    inputs = ['Sales for anyone: ', '<li>Purchase a new tractor blade in the next 24 hours and get one 50% off!', '<li>Become a member and get 20% off your first month.<br>', '<br>Exclusive sales for members: ', '<li>Spend $100 and get a $50 gift card', '<li>Invite someone to become a member and get next months membership FREE! ', '<li>Schedule your winterization this week and get $12 off.']