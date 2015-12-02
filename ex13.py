# when you type python ex13.py to run the ex13.py file, the ex13.py
# is part of a command called an argument.
# this exercise write a script that also accepts arguments.

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# the import is how you add features to your script from the Python feature set.
# argv is the argument variable. holds the arguments you pass to your Python script
# when you run it
# modules = features = libraries
