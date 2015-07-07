__author__ = 'BreenIsALie'

# Exercise 13, Exercises taken from http://learnpythonthehardway.org/book/
# Parameters, unpacking and Variables

# import the argument variable (argv) for use. This is a MODULE (IMPORTANT TO REMEMBER)
from sys import argv

# Take input from argv and assign it to variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

