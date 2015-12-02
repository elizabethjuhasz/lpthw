from sys import argv
from os.path import exist
# doing two imports
# os.path is used because of different operating systems 
# specifies path in different ways

script, from_file, to_file = argv
# specify it when you run the command

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
# taking this info putting it in in_file
indata = in_file.read()
# dot do something to that file. read it.
# indata = open(from_file).read() if this is the case you do not need
# in_file.close() at end. need to remove or get an error message

print "The input file is %d bytes long" % len(indata)
# len = length of the file in bytes

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close()

# one line verison: use semicolon
# from sys import argv; from os.path import exists; script, from_file to_file = argv ; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w') ; out_file.write(indata) ; out_file.close()
