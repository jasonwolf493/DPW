class Calculate(object):
    def __init__(self):
        print "calc init"
        self.__info = []

    #this will simply total everything up and return the total
    def total_up(self, c):
        self.__info.append(c)
        #this is private because only this class will need it
        __holiday_hours = int(c.holiday) * 1.5
        #this is also private
        __holiday_pay = __holiday_hours * int(c.wage)
        #we add up the totals here using some of the private vars above
        total = int(c.wage) * int(c.hours) + __holiday_pay
        print c.biweekly
        #if the paycheck is biweekly its divided by two
        if c.biweekly == "True":
            print "PAY CHECK BIWEEKLY"
            total = total / 2
        else:
            print "PAY CHECK NOT BIWEEKLY"
        return total

    #this will generate some friendly text after getting the total from total_up
    def summary_text(self, c):
        # this will be ran and it will get the total from the totalup
        total = self.total_up(c)
        print total
        print Paycheck.wage
        #then we return that info
        return "Gross: " + str(total)


#this is our dataobject we use this to store the info
class Paycheck(object):
    def __init__(self):
        #default values for paycheck to prevent server from breaking
        self.__biweekly = False
        self.__wage = 0
        self.__hours = 0
        self.__holiday = 0

    #BIWEEKLY GETTER / SETTER

    @property
    def biweekly(self):
        return self.__biweekly

    @biweekly.setter
    def biweekly(self, y):
        self.__biweekly = y

    #WAGE GETTER / SETTER
    @property
    def wage(self):
        return self.__wage


    @wage.setter
    def wage(self, w):
        self.__wage = w

    #HOURS GETTER / SETTER
    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, h):
        self.__hours = h

    #HOLIDAY GETTER / SETTER
    @property
    def holiday(self):
        return self.__holiday

    @holiday.setter
    def holiday(self, h):
        self.__holiday = h
