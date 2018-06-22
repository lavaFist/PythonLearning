from sys import exit

def wall():
    print "You hit a wall! Please try again!"

def find_Award():
    print "Congrats! You find the treasure!"
    exit(0)

def tunel():
    print "A big tunel stands in front of you."
    print "Legend says that there is treasure at the end of tunel."
    print "Do you want to start? Y/N"

    choice = raw_input(">")

    if choice == "N" or choice == "n":
        print "You have no guts, loser!"
        exit(0)
    elif choice == "Y" or choice == "y":
        start()

def direction(direct):
    print "You moved one step", direct

def start():
    print "Choose your direction:\n\tl for left\n\tr for right\n\tf for forward\n\tb for backward"
    index = 0
    while (index < len(map)):
        direct = raw_input(">")
        if direct != map[index]:
            wall()
        else :
            index +=1
            print "You just completed %d correct steps" % index
            if direct == "l":
                direction("left")
            elif direct == "r":
                direction("right")
            elif direct == "f":
                direction("forward")
            elif direct == "b":
                direction("backward")
    find_Award()

def autopilot():
    route = []
    direct = ["l","r","f","b"]
    for item in map:
        for path in direct:
            if path == item:
                route.append(path)
    print route


map = [
    "f","f","f","r",
    "f","f","l",
    "f","l",
    "f","r",
    "f","f","f","f","r",
    "f","r",
    "l",
    "f","r",
    "l",
    "r",
    "l",
    "r",
    "f","f","r",
    "f","l",
    "l",
    "f","r",
    "f","f","r",
    "f","f","r",
    "r",
    "f","l",
    "l",
    "f","r",
    "f"
    ]
