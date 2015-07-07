__author__ = 'BreenIsALie'

# Exercise 11, Exercises taken from http://learnpythonthehardway.org/book/

# Prompt user for information, and store info in variables
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# Return all inputted info as formatted string
print "So, you are %r old, %r tall and %r heavy" % (age, height, weight)

