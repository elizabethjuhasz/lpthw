from sys import argv
# argument variable. taking things and squishing it

script, filename = argv

txt = open(filename)
# we are creating a variable called txt

print "Here's your file %r:" % filename
print txt.read()

# dot is an operator.  take the object (txt) and then read it.

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# close a file
txt.close
txt_again.close
