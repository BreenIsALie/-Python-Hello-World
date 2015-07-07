__author__ = 'BreenIsALie'

# Exercise 14, Exercises taken from http://learnpythonthehardway.org/book/
# Prompting and passing
# Taking input from users when starting the script (like arguments when running linux commands)

from sys import argv

script, user_name = argv # take input from argv and assign to variables
prompt = '> ' # Give users a nice looking prompt

# Print the information gathered back to users
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Return all the info to the user
print """
Alright, so you said %r about liking me
You live in %r. Not sure where that is
And you have a %r computer. Nice
""" % (likes, lives, computer)

