__author__ = 'BreenIsALie'

# Exercise 8, Exercises taken from http://learnpythonthehardway.org/book/

# Initiate formatter and tell it to use 4 variables
formatter = "%r %r %r %r"

# Uses formatter with numeric variables
print formatter % (1, 2, 3, 4)
# Uses formatter with string variables
print formatter % ("one", "two", "three", "four")
# Uses formatter with boolean variables
print formatter % (True, False, False, True)
# Uses formatter with the text string from line line 6, prints 4 times (lots of %r's)
print formatter % (formatter, formatter, formatter, formatter)
# Uses formatter with the text string seen below. Comma keeps it to one line instead of using line breaks
print formatter % ("I had this thing.",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So i said goodnight"
                    )
