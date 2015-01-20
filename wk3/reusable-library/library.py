class Calculate(object):
    def __init__(self):
        print "calc init"
        self.__info = []

    #this will simply total everything up and return the total
    def total_up(self, c):
        self.__info.append(c)
        __holiday_hours = c.holiday * 1.5
        __holiday_pay = __holiday_hours * c.wage
        total = c.wage * c.hours + __holiday_pay
        #print c.wage
        #print total
        return total

    #this will generate some friendly text after getting the total from total_up
    def summary_text(self, c):
        total = self.total_up(c)
        print total
        return "Gross: " + str(total)



class Paycheck(object):
    def __init__(self):
        self.__biweekly = False
        self.__wage = 0 #check if meets federal minimum wage
        self.__hours = 0
        self.__holiday = 0

    #BIWEEKLY GETTER / SETTER
    @property
    def biweekly(self):
        pass

    @biweekly.setter
    def biweekly(self, y):
        self.__biweekly = y
"""
    #WAGE GETTER / SETTER
    @property
    def wage(self):
        pass

    @wage.setter
    def wage(self, w):
        self.__wage = w

    #HOURS GETTER / SETTER
    @property
    def hours(self):
        pass

    @hours.setter
    def hours(self, h):
        self.__hours = h

    #HOLIDAY GETTER / SETTER
    @property
    def holiday(self):
        pass

    @holiday.setter
    def holiday(self, h):
        self.__holiday = h

"""