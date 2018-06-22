from sys import argv

script, filename = argv

#read file based on parameter when called this script
txt = open(filename)
print "Here's your file %r" % filename
print txt.read()
txt.close()

#read file based on file name input from cmdline
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
