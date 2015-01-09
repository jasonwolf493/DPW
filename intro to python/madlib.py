__author__ = 'Jason'
#give ready a default value
ready = ""

#neat little trick to clear terminal
clear = chr(27) + "[2J"

#dwarves have a couple names, Dictionaries are perfect for that!
dwarves = dict()
dwarves = {"larry":"Ronan Coppertapper", "joe":"Goraidh Redboron"}

#If user is not ready lets do this.
while ready != "yes":
    print clear

    #check if user is talking correctly
    if ready == "y":
        print "Excuse me but we speak in full sentences here!"
        print "Are you ready? Yes or no?"
    else:
        print "What's this gibberish coming out of your mouth? Just say 'yes' when you're ready."
    #the title
    print "The Great Journey"

    #now lets see if the user is ready.
    ready = raw_input("Are you ready to begin? ")
    print clear

#if the user finally decides they're ready and they are using full words lets continue
if ready == "yes":
    #~~~~~~~~~~ LETS GATHER SOME INFO! ~~~~~~~~~~~~~~~~~~
    print "Please enter the following info and a story shall be generated for you"

    #get the adventurers name so we can call them something
    name = raw_input("Enter your name: ")
    print clear

    loner = raw_input("Are you a loner: ")
    print clear

    ale = raw_input("Enjoy ale?: ")
    print clear

    ale_type = raw_input("A type of fish: ")
    print clear

    number1 = raw_input("Enter a number: ")
    print clear

    number2 = raw_input("Enter yet another number: ")
    print clear

    age = raw_input("Enter your age: ")
    print clear

else:
    exit()

#the magical pen writes the story on the scroll
def tell_story(name, loner, ale, ale_type, number1, number2, age):
    year = number1 + number2

    #first part
    story_text = """
The story begins here, it was the year of {year} a short one, but a historic one! It was a typical dwarvish
night, everyone was gathered at the tavern of course! Though it was calm, brisk night and only the crickets
were out, you could hear clinking of glasses and loud dwarves inside the tavern.
    """

    #second part
    if loner == "yes":
        loner_story = "\nInside the tavern sat a young dwarf, " + name + " was only " + age + " back then. Back then " + name + " was very shy, they\n could always be found in the same corner of the tavern."
    else:
        loner_story = "\nInside the tavern sat a young dwarf, " + name + " was only " + age + " back then. Back then " + name + " was very outgoing, they\n could always be found at the same table of the tavern with the group of dwarves. " + dwarves["joe"] + " and " + dwarves["larry"] + " were two regulars also."

    #third part
    if ale == "yes":
        ale_story = "\n" + name + " was fond of the crisp bubbly " + ale_type + "-ale that the tender slammed on the table. Though " + name + " was frightened\n by the thought of " + ale_type + ", " + name + " was sure that the name had nothing to do with actual " + ale_type
    else:
        ale_story = "\n" + name + " was furious that such a coward would consider even setting this ale within their sight. " + name + " swung their arm across\n the table causing the ale to go flying across the tavern, the giant Dwarf sized beer mug smashed the wall causing the " + ale_type + "-ale to splash. The loud tavern silenced for a few seconds then went back to its normal self."

    #format the global vars so we can use them in docstring
    story_text = story_text.format(**locals())

    #send all the story parts back in the right order!
    return story_text + loner_story + ale_story

#set story to = the tell_story return
story = tell_story(name, loner, ale, ale_type, number1, number2, age)

#then print it so we can read our story
print story

