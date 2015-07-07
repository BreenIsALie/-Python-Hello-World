__author__ = 'BreenIsALie'

# Exercise 10, Exercises taken from http://learnpythonthehardway.org/book/
# Escape sequences

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

# \t creates a tabbed space
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Unsure exactly what this does, apart from using a lot of CPU resources for 15 sec or so
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,