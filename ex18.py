def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_two_gain(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "Not a thing"

print_two("Have", "Fun")
print_two_gain("More", "Fun")
print_one("Single")
print_none()
