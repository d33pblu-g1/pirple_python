# Homework Assignment #4: Lists
#
# Details:
#
# Create a global variable called myUniqueList. It should be an empty list to
# start.
#

myUniqueList = []
myLeftovers = []

# Next, create a function that allows you to add things to that list. Anything
# that's passed to this function should get added to myUniqueList, unless its
# value already exists in myUniqueList.

listCount = -1
tryCount = 0

# If the value doesn't exist already, it
# should be added and the function should return True.
def repeatSecondCounterFnct(inputIntoList):
    global listCount
    global tryCount

    if tryCount < listCount:
        tryCount += 1
        UniqueCheck(inputIntoList)
    else:
        listCount += 1
        myUniqueList.append(inputIntoList)
        print("True")


#If the value does exist,
# it should not be added, and the function should return False;

# check for uniqueness
def UniqueCheck(inputIntoList):
    global tryCount
    if myUniqueList[tryCount] == inputIntoList:
        myLeftovers.append(inputIntoList)
        print("False")
    else:
        repeatSecondCounterFnct(inputIntoList)

def addToList(inputIntoList):
    global listCount
    global tryCount

    # first input only
    if listCount == -1:
        myUniqueList.append(inputIntoList)
        listCount += 1
    # second input and onwards
    elif listCount > -1:
        tryCount = 0
        UniqueCheck(inputIntoList)


# Finally, add some code below your function that tests it out. It should add a
# few different elements, showcasing the different scenarios, and then finally
# it should print the value of myUniqueList to show that it worked.


addToList("one")
addToList("two")
addToList("three")
addToList("three")
addToList("four")
addToList("five")
addToList("one")
addToList("four")

# print out reslts
print("\n")
print("Unique inputs:")
print(myUniqueList)

#
#
# Extra Credit:
#
# Add another function that pushes all the rejected inputs into a separate
# global array called myLeftovers. If someone tries to add a value to
# myUniqueList but it's rejected (for non-uniqueness), it should get added to
# myLeftovers instead.

print("\n")
print("Duplicate inputs:")
print(myLeftovers)
