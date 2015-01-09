#one lined comment

'''

Doc strings
'''

print "Hello World"

first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name: ")
#print "hello, " + response

birth_year = 1965
current_year = 2015
age = current_year - birth_year
print "you are " + str(age) + " years old"


'''
if age >= 50:
    print "you are over 50yrs old"
elif age <= 48:
    print "you are under 49yrs old"
else:
    print "you are 49yrs old"

'''

character = ["jason","ange","brad"]
character.append("kitty")
print character[0] +" " + character[1]

movies = dict()
movies = {"starwars":"darth vader", "silence of the lambs":"Hannibal Lecter"}
print movies["starwars"]


'''
i = 0
while i<9:
    print "the count is", i
    i = i + 1

for i in range(0,10):
    print "the count is", i
    i = i + 1

'''

def calcArea(h,w):
    area = h * w
    return area

a = calcArea(20, 40);
print "My area is",a,"sqft"


title = "Contact Us"
body = "You can contact us at 555-555-5555"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''

message = message.format(**locals())
print message


