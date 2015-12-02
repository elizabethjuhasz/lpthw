# combining argv and raw_input

from sys import argv
script, user_name = argv
# the script, plus the username for the argument. (argv is looking for
# two things). 

prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
And you live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# prompting:  asking for information
# passing: putting into the right place

% format activator
# triple quotes, you can put as many lines as you want.  will understand
# the breaks

 
