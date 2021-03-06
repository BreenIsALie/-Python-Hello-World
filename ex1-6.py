__author__ = 'BreenIsALie'

# Initial Hello World environment test. Random basic code snippets abound below. Test of GitHub functions. This covers exercise 1 through 6 from http://learnpythonthehardway.org/book/

print "Hello World"
print "Goodbye"

# Math below
print "Addition:", 20 + 30
print "Subtraction:", 50 - 20
print "Division:", 50 / 2
print "Multiplication", 5*5

# Logical operators
print "Is 3+2 bigger then 5-7?"
print 3 + 2 < 5 - 7

print "What is 3 + 2", 3+2
print "What is 5 - 7", 5-7

print "Below is code relating to 5 and -2"
print "Is 5 greater then -2 ?", 5 > -2
print "is 5 greater or equal to -2?", 5>=-2
print "Is 5 less or equal to -2?", 5 <=-2

# Tests using floating point

print "Print 20 as a float number", 20.0
print "print 30 as a float number", 30.0

print "Add together", 20.0 + 30.0

print "Now with more decimals"
print 20.5 + 30.5

# Variable tests below
# Logic + variables to print info

cars = 100
space_in_a_car = 4.0
drivers = 30
cars_driven = drivers
passengers = 90
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passengers / cars_driven

# Print results from above code
print "There are", cars, "cars avalible"
print "There are only", drivers, "drivers avalible"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passanger_per_car, "in each car"

# Format strings and variables
my_name = "BreenIsALie"
my_age = "22"
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s" % my_name
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" %my_teeth

# Math using the variable string
num1 = 10
num2 = 20
num3 = 30

print "If i add %d, %d and %d i get %d" % (num1, num2, num3, num1 + num2+ num3)

# More text and strings
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e