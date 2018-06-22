"""
This is a sample of script, you need to key in same number of
variables to use this script. In this case, the number of variables
is 3. So following is an example on how to use this script:
    python ex13.py this is sample
"""
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

others = raw_input("Anything else you want to add?\t")
print "%r" %others
