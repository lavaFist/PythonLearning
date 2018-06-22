print "You enter a dark room with 2 doors, which door do you want to go through? \n Door #1 or Door #2"

door = raw_input(">")

if door == "1":
    print "There is a giant bear eating a cheese cake. What do you do?"
    print "1) Take the cake"
    print "2) Scream at the bear"

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats you instead, you are dead!"
    elif bear == "2":
        print "The bear runs at you and killed you, you are dead!"
    else:
        print "Well done! Doing %s maybe better, the bear runs away!" % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina"
    print "1) Blueberries"
    print "2) Yellow jacket clothespins"
    print "3) Understanding revolvers yelling melodies"

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello, well done!"
    else:
        print "The insanity rots your eyes into a pool of muck. you are blind!"

else:
    print "You stumble around and fall on a knife and dead!"
