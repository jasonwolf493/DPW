__author__ = 'Jason'

#class to calculate users insurance quote
# use car type ex. sports economy truck
# accident history
# car value
# coverage amount


class GenerateQuote(object):
    def __init__(self):
        self.vehicle_type = ""
        self.recent_incident = ""
        self.__car_value = 0
        self.__coverage_amount = 0
        self.__total_coverage = 0  # How much will have to be covered coverage_amount + car val

    # Getter and Setter for the private __car_value
    @property
    def car_value(self):
        return self.__car_value

    @car_value.setter
    def car_value(self, v):
        if v < 1:
            print "invalid car val"
            self.__car_value = 500
        else:
            self.__car_value = v + 1000

    # Getter and setter for the private coverage amount
    @property
    def coverage_amount(self):
        return self.__coverage_amount

    @coverage_amount.setter
    def coverage_amount(self, a):
        if a > 0:
            print "Cov amount greater than 0"
            self.__coverage_amount = a + self.car_value
        else:
            self.__coverage_amount = 20000

    # property for the private __total_coverage sets a total amount that will be covered
    @property
    def total_coverage(self):
        self.__total_coverage = self.car_value + self.coverage_amount
        return self.__total_coverage



