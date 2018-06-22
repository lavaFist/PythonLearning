from sys import exit

def gold_room():
    print "This room is full of gold, How much will you take?"

    choice = raw_input(">")
    if "0" in choice or "1" in choice:
        how_much = int (choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you are not greed, here's your gold!, Good job"
        exit(0)
    else:
        dead("You greedy basterd!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_move = False

    while True:
        choice = raw_input(">")

        if choice == "take honey":
            dead ("The bear slaps your face off!")
        elif choice == "taunt bear" and not bear_move:
            print "The bear has moved"
            bear_move = not (bear_move)
        elif choice == "taunt bear" and  bear_move:
            print "You step into the door and you find..."
            gold_room()
        else:
            print "I have no idea what your action is..."

def cthulhu_room():
    print "Here you see the great evil cthulhu."
    print "He, it, whatever stars at you and you go insane."
    print "Do you flee for you life or eat your head?"

    choice = raw_input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why ,"You are dead!"
    exit (0)


def start():
    print "You are in a dark room."
    print "There are 2 doors, one on your left and another on your right."
    print "Which one you want to go?"

    door = raw_input(">")

    if door == "left":
        bear_room()
    elif door == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve!")


start()
