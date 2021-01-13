################################################################################
################################################################################
#####
##### IMPORT Python functions
#####
################################################################################
################################################################################

# import everything from the math libary
from math import *


################################################################################
################################################################################
#####
##### Strings
#####
################################################################################
################################################################################

# to print a new line use \n
print ("Line1\nLine2")

# to print a quotation mark " use \"
print ("this is a quotation mark \"")

# concatenation
First_name = "Michael"
Second_name = "Phitides"
print (First_name + " " + Second_name)

# uppercase
print(First_name.upper())

# lowercase
print(First_name.lower())

# check if something is uppercase
UPPER = "ASD"
print (UPPER.isupper())

# count the lenght use len()
count_the_characters = len(First_name)
print(count_the_characters)

# to pick one character from the string user []
# remember to start with 0
print(First_name[0])

# to find a specific character in a string use index()
print(First_name.index("cha"))

#to replace a string with another
print(First_name.replace("M","/\/\ "))
print(First_name)

var = "10"
print("asd"+"asd"+var)

################################################################################
################################################################################
#####
##### Numbers
#####
################################################################################
################################################################################

# add 1 to counter
counter = 0
counter += 1

# mod - remainder
print("calculating remainders:")
print(10%3)

#convert number into a string
fav_number = 25
print("my favourite number is " + str(fav_number))
print("\n")

#absolute values
print(abs(-5))
print("\n")

# powers
print(pow(3,2))
print("\n")

#return the max from a list
print(max(1,2,3))
print("\n")

#return the min from a list
print(min(1,2,3))
print("\n")

# rounding
print("to round a number use round()")
print("eg round(3.7)")
print(round(3.7))
print("\n")

# round down
print(floor(3.7))

#round up
print(ceil(3.7))

#square root
print(sqrt(2))

# convert string to Integer
num1 = "2"
num2 = "3"
print(int(num1)+int(num2))
################################################################################
################################################################################
#####
##### Input
#####
################################################################################
################################################################################

#name = input("enter name:")
#print("I Love you "+name)

################################################################################
################################################################################
#####
##### Numbers
#####
################################################################################
################################################################################


################################################################################
################################################################################
#####
##### Lists
#####
################################################################################
################################################################################
print("#######")
print("Lists"+"\n")

# TestList = ["Element1","Element2","Element3"]
ShoppingList = ["eggs","bacon","bread","sausage","juice"]
print(ShoppingList[0])
print(ShoppingList[1])
print(ShoppingList[2])
print(ShoppingList[-1])

#from - to (but not including)
print(ShoppingList[0:3])
print(ShoppingList[0:-2])

# start from an element until the end
print(ShoppingList[0:])
print(ShoppingList[2:])

#edit one Element
ShoppingList[0] = "Mushrooms"
print(ShoppingList)

# remove an element

#to remove element position 2 - remember that a list starts at 0
ShoppingList[1:2]=[]
print(ShoppingList)

# add a list in a List
ShoppingList[3]=[]
print(ShoppingList)
ShoppingList[3]=["apple juice","orange juice", "grapefruit juice"]
print(ShoppingList)

#access an element within a list which is within a List
print(ShoppingList[3])
print(ShoppingList[3][1])

# append to the list
ShoppingList.append("jam")
print(ShoppingList)

################################################################################
################################################################################
#####
##### FUNCTIONS
#####
################################################################################
################################################################################




################################################################################
################################################################################
#####
##### ASD
#####
################################################################################
################################################################################
# print("#######")
# print("ASD"+"\n")
