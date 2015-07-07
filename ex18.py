__author__ = 'BreenIsALie'

# Exercise 18, Exercises taken from http://learnpythonthehardway.org/book/
# Names, variables, code and functions

# initiate the first function
def print_two(*args):
        arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)

# Same function as above, but slimmer code
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Same functionality, but with a single argument
def print_one(arg1):
    print "arg1: %r" % arg1

# Same as above, but with no arguments
def print_none():
    print"I got nothin'"

# Calling the defined function from above

print_two ("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

