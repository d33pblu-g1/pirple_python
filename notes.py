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

# to print on the same Line
print("this will be on the same line as ",end="")
print("this line")


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

#convert number received from an input into an intiger
number1 = input("enter a number: ")
number2 = input("enter another number: ")
result1 = number1 + number2
result2 = int(number1) + int(number2)
print("number1 + number2 :")
print(result1)
print("int(number1)+int(number2) :")
print(result2)


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

name = input("enter your name:")
print("Hi "+name)





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
##### Loops
#####
################################################################################
################################################################################

# FOR LOOPS
Word = "hello"

for w in Word:
    print(w)
    if w == "e":
        print("what a funny letter")


list = [1,2,3]
counterl = 0
for w in list:
    print(list[counterl])
    counterl +=1


# RANGE
# range(start,stopping,increment steps)
for num in range(10):
    print(num)

#example all odd numbers
for num in range(1,100,2):
    print(num)
#example 2
for num in range(-100,-1,2):
    print(num)

# example 3
X = 'abcd'
for i in range(len(X)):
    print(i)

# WHILE LOOPS

counter = 1
while (counter <10):
    print(counter)
    counter += 1

# Infinite loops
while(True)
# the above also means while(true == true)

# break - is used to terminate the loop
listOfNames = ["Mike","Pauline","Kai","Summer","Sophie"]

for x in range(len(listOfNames)):
    if listOfNames[x] == "Summer":
        break
print(x+1)

# another example
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1


# continue - stop and continue the loop (do not execute from here on)

for number in range(10):
    if number%2 == 0:
        print(str(number) + " is even")
        continue # skip the rest
    print(str(number) + " is odd")



################################################################################
################################################################################
#####
##### SETS
#####
################################################################################
################################################################################

# sets remove duplicates
sets = {"element1", "element2", "element1", "element4"}
print(sets)

#example
CountryList = []
for i in range(5):
    Country = input("Please enter your country:")
    CountryList.append(Country)

CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)

if "Brazil" in CountrySet
    print("Yes")

################################################################################
################################################################################
#####
##### Dictionary
#####
################################################################################
################################################################################


dic1 = {"key1":"value1","key2":"Value2","key3":"Value3"}
print(dic1)


# EXAMPLE 1
CountryList = []
for i in range(5):
    Country = input("Please enter your country:")
    CountryList.append(Country)


CountryDictionary = {}

for Country in CountryList:
    if Country in CountryDictionary:
            CountryDictionary[Country] += 1
    else:
        CountryDictionary[Country] = 1

print(CountryDictionary)

# EXAMPLE 2

BlackShoes = {42:2,41:3,40:4,39:1,38:0}
print(BlackShoes)
while(True):
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if purchaseSize < 0:
        break
    if BlackShoes[purchaseSize] > 0:
        BlackShoes[purchaseSize] -= 1
    else:
        print("No shoes in stock")
    print(BlackShoes)


print(BlackShoes)
################################################################################
################################################################################
#####
##### ASD
#####
################################################################################
################################################################################
# print("#######")
# print("ASD"+"\n")

################################################################################
################################################################################
#####
##### examples
#####
################################################################################
################################################################################

num1 = input("enter the first number: ")
num2 = input("Enter a second number: ")
result = int(num1) + int(num2)
print(result)
