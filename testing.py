# Homework Assignment #7: Dictionaries and Sets
#
#
# Details:
#
# Return to your first homework assignments, when you described your favorite
# song. Refactor that code so all the variables are held as dictionary keys and
# value.

# Setting Variables
Band = {"Name":"Linkin Park","Genre":"Rock","Formed":"1996","Vocalist":"Mike Shinoda","Guitarist":"Brad Delson","Bassist":"Dave Farrell","DJ":"Joe Hahn","Drummer":"Rob Bourdon"}

# Then refactor your print statements so that it's a single loop that
# passes through each item in the dictionary and prints out it's key and then
# it's value.

keys = list(Band.keys())
print(keys)

for i in range(len(Band)):
    print(keys[i] +": " ,end="")
    print(Band[keys[i]])

#
#
# Extra Credit:
#
# Create a function that allows someone to guess the value of any key in the
# dictionary, and find out if they were right or wrong. This function should
# accept two parameters: Key and Value. If the key exists in the dictionary
# and that value is the correct value, then the function should return true.

# In all other cases, it should return false.
while True:
    GuessInput = input("guess")
    if GuessInput != "exit":
        continue

    break
