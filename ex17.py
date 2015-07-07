__author__ = 'BreenIsALie'

# Exercise 17, Exercises taken from http://learnpythonthehardway.org/book/
# Additional code related to files, this copies the file

from sys import argv  # Allows for input from the command line when opening the file
from os.path import exists  # Uses OS functions to check if files exist

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)   #Checks the file length using len

print "Does the output file exist ? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()  # Ask for confirmation

out_file = open(to_file, "w")
out_file.write(indata)

print "All done"

# Close both files
out_file.close()
in_file.close()


