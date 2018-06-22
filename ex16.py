from sys import argv
script, filename = argv

print "We are about to erease %r" %filename
print "If you don't want to proceed, please hit ctrl+c"
print "Hit RETURN to proceed"
raw_input("?")

print "File opening ... "
target = open(filename, 'w')

print "Truncating the file, please wait..."
target.truncate()

print "Now I'm going to write 3 lines to the file"

line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input("line 3 :")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "Action completed, close the file"
target.close()

print"Open the new file again"
target = open(filename)
print target.read()
target.close()
