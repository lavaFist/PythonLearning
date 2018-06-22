print "I will calculate how many chickens:"

print "Hens", 25 + 30 / 6 #30
print "Roosters", 100 - 25 * 3 % 4 #97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#when calculating 1 / 4 + 6, due to "1" doesnt have any floating  point,
#result is dropping the part after decimal, seems like a round down, and it is 6
#However, if formula is "1.0 / 4 + 6", then result will be 6.25

print 7/4
print 7.0/4.0

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7 #false

print "what is 3 + 2", 3 + 2 # 5
print "what is 5 - 7", 5 - 7 #-2

print "Oh, that is why it is false"

print "how about more"

print "is it greater?", 5 > -2 #true
print "is it greater or equal", 5 >= -2 # true
print "is it less or equal?", 5<= -2 #false
