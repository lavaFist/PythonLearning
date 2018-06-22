from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

indata = open(from_file).read()

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, ctrl+c to abort"
raw_input("Go?")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Task completed"

out_file.close()
