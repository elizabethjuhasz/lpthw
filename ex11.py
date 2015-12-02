print "How old are you?",
age = raw_input ()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# we put a , (comma) at the end of each print line.  This is so that print
# end a new line and go to the next line
# the difference between the input() and raw_input() is that input()
# will try to convert things you enter as if they were Python code, but it has security
# problems so you should try and avoid
# raw_input gets info from the user and returns the data input by the user in a string.

name = raw_input("what is your name? ")
print "Hello, %s." % name
