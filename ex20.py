__author__ = 'BreenIsALie'

# Exercise 19, Exercises taken from http://learnpythonthehardway.org/book/


from sys import argv  # Import the arguments from the command line running of the script

script, input_file = argv  # Save external arguments to script (script name) and input_file (selected file)

# Function for printing all of a file
def print_all(f):
    print f.read()

# Function for moving the "read head" to the start of the file
def rewind(f):
    f.seek(0)

# Function for printing the line count of a file
def print_a_line(line_count, f):
    print line_count, f.readline()

# Opens the selected file for reading, and saves it in current_file
current_file = open(input_file)

print "First, lets print the whole file:\n"

# Prints everything in the opened file
print_all(current_file)

print "Now lets rewind, kind of like a tape"

rewind(current_file)

# This section uses current_line to select which line to use, and increments it once for each run
# Could be used in a loop as well
print "Lets print three lines"
current_line = 1
print_a_line(current_line, current_file)  # selects current line of current file. Line incremented for each run

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
