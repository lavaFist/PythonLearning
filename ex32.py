the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go though mixed list too
for i in change:
    print "I got %r" % i

elements = range (0,6)

for element in elements:
    print "New item in list is %s " % element
