# Homework Assignment #6: Advanced Loops
#
#
# Details:
#
# Create a function that takes in two parameters: rows, and columns, both of
# which are integers.

def drawBoard(rows,columns):

# The function should then proceed to draw a playing board
# (as in the examples from the lectures) the same number of rows and columns as
# specified.
    if rows <= 12 and columns <=120:
        for r in range(0,rows):
            if r%2 == 0:
                for c in range(0,columns):
                    if c%2 == 0:
                        if c == columns-1:
                            print(" ")
                        else:
                            print(" ",end="")
                    else:
                        if c == columns-1:
                            print("|")
                        else:
                            print("|",end="")
            else:
                print("-"*(columns+1))

# After drawing the board, your function should return True.
        return True
    else:
        return False

drawBoard(10,100)

#
# Extra Credit:
#
# Try to determine the maximum width and height that your terminal and screen
# can comfortably fit without wrapping. If someone passes a value greater than
# either maximum, your function should return False.
