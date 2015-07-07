__author__ = 'BreenIsALie'

# Exercise 14, Exercises taken from http://learnpythonthehardway.org/book/
# Read and write to files. This script is a text editor

# Import argv for use with command line
from sys import argv

script, filename = argv  # take the script name and a file to open from command line

print "We are going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN"

raw_input("?")  # Ask the user for confirmation

print "Opening the file..."
target = open(filename, "w")  # Open the file specified by the command line

print "Truncating the file. Goodbye!"
target.truncate()  # Erase the file content

print "Now i'm going to ask you for three lines"

# User input goes here
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file"

# Write each line (taken from the user input variable) to a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file, ending the interaction
print "And finally, we close it"
target.close()
