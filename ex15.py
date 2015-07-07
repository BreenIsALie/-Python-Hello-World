__author__ = 'BreenIsALie'

# Exercise 14, Exercises taken from http://learnpythonthehardway.org/book/
# Reading info from files

# Import argv module for use
from sys import argv

# Take command line input and save to variables
script, filename = argv

# txt function opens the file specified when starting the script. Ex 'python ex15.py ex15_sample.txt'
txt = open(filename)

print "Here's your file %r" % filename
print txt.read() # Read the contents of the text file and present to user

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again) # takes the file the user specified inside the script and reads contents

print txt_again.read() # prints content to user





