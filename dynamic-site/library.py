__author__ = 'Jason'

# Fill in the contact info with some info here


class GeneratePage(object):  # this has every attribute we'll need
    def __init__(self):
        self.link = ""  # We use this to determine raises or lowers the risk factor






    #risk calculation to make riskier drivers pay more
    @property
    def car_type_risk(self):  # check the kind of car, and recent incidents then calculate risk accordingly
        if self.link == "form":
            print "is form page"
            if self.recent_incident == "Yes":
                self.__risk = 150
                return self.__risk
            else:
                self.__risk = 100
                return self.__risk
        else:
            self.__risk = 0
            print "Other"
            return self.__risk

    @property
    def monthly_cost(self):  # Calculate monthly payment, we take the total coverage and divide it by 10 years
        self.__monthly_cost = (self.total_coverage/180)+self.car_type_risk
        return self.__monthly_cost
          # we also make sure we add the risk in after.
# 180 MONTHS OR 15 YEARS

    # Getter and Setter for the private __car_value
    @property
    def car_value(self):
        return self.__car_value

    @car_value.setter
    def car_value(self, v):  # use the customers input

        if v < 1:
            print "invalid car val"
            self.__car_value = 500
        else:
            self.__car_value = v

    # Getter and setter for the private coverage amount
    @property
    def coverage_amount(self):
        return self.__coverage_amount

    @coverage_amount.setter
    def coverage_amount(self, a):
        if a > 0:  # Make sure they have at least added some coverage
            print "Cov amount greater than 0"
            self.__coverage_amount = a
        else:  # if for some reason they don't we add 20000
            print "adfda"
            self.__coverage_amount = 20000

    # property for the private __total_coverage sets a total amount that will be covered
    @property
    def total_coverage(self):
        self.__total_coverage = int(self.car_value) + int(self.coverage_amount)
        return self.__total_coverage



