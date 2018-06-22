ten_thing ="Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list, let's fix that."

stuff = ten_thing.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

'''
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: %s" % next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)
'''

for item in stuff:
    if len(stuff) < 10:
        new_item = more_stuff.pop()
        print "Adding: %s" % new_item
        stuff.append(new_item)
        print "There are %d items now" %len(stuff)


print "There we go: ", stuff

print "Let's do some thing with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print ' '.join(stuff[3:5])
