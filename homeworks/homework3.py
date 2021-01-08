# Homework Assignment #3: "If" Statements
#
#
# Details:
#
# Create a function that accepts 3 parameters and checks for equality between
# any two of them.
#
# Your function should return True if 2 or more of the parameters are equal,
# and false is none of them are equal to any of the others.
#
#
# Extra Credit:
#
# Modify your function so that strings can be compared to integers if they are
# equivalent. For example, if the following values are passed to your function:
#
# 6,5,"5"
#
# You should modify it so that it returns true instead of false.
#
# Hint: there's a built in Python function called "int" that will help you
# convert strings to Integers.

###############################################################################
###############################################################################
###############################################################################

#Define variables
Hungry = False
Time = 0
TypeOfMeal = "unknown"

# set the time to new value
def TimeSetting(NewTime = 0):
    global Time
    Time = NewTime

#set hunger Level - boolean
def SetHunger(NewHungerLevel = False):
    global Hungry
    Hungry = NewHungerLevel

#Imput time
TimeSetting(1330)

#Imput Hunger True/False
SetHunger(True)

#Decision
if Hungry == True and Time >= 800 and Time < 900:
    TypeOfMeal = "Breakfast"
    print("it is",Time,"and you are hungry. You should eat", TypeOfMeal,".")
elif Hungry == True and Time >=1300 and Time < 1400:
    TypeOfMeal = "Lunch"
    print("it is",Time,"and you are hungry. You should eat", TypeOfMeal,".")
elif Hungry == True and Time >=1900 and Time < 2000:
    TypeOfMeal = "Dinner"
    print("it is",Time,"and you are hungry. You should eat", TypeOfMeal,".")
elif Hungry == True:
    print("it is",Time,"and you are hungry. You should eat a banana")
else:
    print ("it is",Time,"No need to eat. You are not hungry!")
