__author__ = 'Jason'

# Fill in the contact info with some info here


class GeneratePage(object):  # this has every attribute we'll need
    def __init__(self):
        self.link = ""  # We use this to determine raises or lowers the risk factor


class GenerateInputs(object):
    inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]


class GenerateContacts(object):
    inputs = ['Phone: ', '1-555-555-5555', 'Email: ', 'FakeEmail@Fake.com', 'Address: ', '1234 placeholder blv. USA']