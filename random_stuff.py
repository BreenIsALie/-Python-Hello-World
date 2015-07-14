__author__ = 'BreenIsALie'

# Place to test random stuff, following no special tutorial or guide. This is a simple loop test
# with user set exit conditions

# Function to check for exit conditions. Currently the condition is the user writing "end"
def CheckForExit():
    x = 0
    if raw_input("\n:> ") == "end":
        return 1
    else:
        return 0

StopCondition = 0

while StopCondition != 1:
    print "Type end to exit, otherwise press enter to continue"

    StopCondition = CheckForExit()

    if StopCondition == 1:
        break
    else:
        StopCondition == 0

print "Loop has finished"

