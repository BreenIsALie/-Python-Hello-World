__author__ = 'BreenIsALie'

# Exercise 21, Exercises taken from http://learnpythonthehardway.org/book/

# Function doing additions
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

# Function doing subtraction
def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

# Function doing multiplication
def multiply (a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

# Function doing division
def divide (a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Lets do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes;", what, "Can you do it by hand"