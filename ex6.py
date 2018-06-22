x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary, do_not)

print x
print y

print "I sad: %r" % x
print "I also said: '%s'" % y

hilarous = True
joke_evaluation = "Isn't that joke so funny? %r"


print joke_evaluation % hilarous
#%r take the value of hilarous and be part of print, cannot use "+" bcs hilarous is not a string type

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
