
# | | | | | | | |
# | | | | | | | |
# | | |O| | | | |
# | | |X|X|O| | |
# | |O|O|X|O| | |
# | |X|X|O|X| | |
#


import os
from time import sleep

# First Set up the board size
# boardsize = input("what is the board size")
BoardCols = 7
BoardRows = 6


#set player 1 to start
Player = 1
UserSymbol = "X"

# Global variable that shows the column selection of the user
UserInputCol = 0

CheckStringHor = ""
CheckStringVer = ""
CheckStringDia = ""
CheckStringDiaDown = ""

Result = ""


# define clear function
def clear():
    _ = os.system('cls')

# create all the fields based on the Board Columns and Rows
currentField = []
for row in range(BoardRows):
    currentField.append([])
    for cols in range(BoardCols):
        currentField[row].append(" ")

def BuildBoard(BoardRows,BoardCols,currentField):
    clear()
    # number first row
    #the last one should have a line break
    rownum = 1
    for cols in range(BoardCols-1):
        print("",str(rownum),end="")
        rownum += 1
    print("",rownum)

    # build the rows (need to go backwards)
    for rows in range(BoardRows-1,-1,-1):

        # build the columns by adding the "|" or spaces.
        for cols in range(1,BoardCols*2+2):
            # last character should be "|" with the default line break that comes
            # with the print function
            if cols == BoardCols*2+1:
                print("|")
            # all odd characters should have a "|"
            elif cols%2 != 0:
                print("|",end="")

            # all even characters should have a the values entered by the players " "
            else:
                print(currentField[rows][int(cols/2-1)],end="")
                # print(rows,int(cols/2),end="")
#    print(CheckStringHor)

BuildBoard(BoardRows,BoardCols,currentField)

def ChangePlayer():
    global Player
    global UserSymbol
    if Player == 1:
        UserSymbol = "O"
        Player = 2
    else:
        UserSymbol = "X"
        Player = 1
    #return UserSymbol


def FindEmptyRow(UserInputCol,UserSymbol):
    counter = 1
    for i in currentField:

        if i[UserInputCol-1] == " ":
            i[UserInputCol-1] = UserSymbol
            ChangePlayer()
            break
        else:
            if counter == BoardRows:
                print("we are full buddy")
                sleep(2)
            counter += 1

#        print(counter)

#    print(currentField)


def MakeHorStr():
    global CheckStringHor
    CheckStringHor = ""
    for i in currentField:
        for j in i:
            CheckStringHor = CheckStringHor + j

def MakeVerStr():
    global CheckStringVer
    global BoardRows
    global BoardCols
    ColsCounter = 0
    CheckStringVer = ""
    while ColsCounter < BoardCols:
        for i in range(BoardRows):
            CheckStringVer = CheckStringVer + currentField[i][ColsCounter]
        ColsCounter += 1

def MakeDiaStr():
    global CheckStringDia
    global BoardRows
    global BoardCols
    for a in range(BoardRows):
    # 6 lopps (as many as the rows)
        #print("a=",a)
        for b in range(BoardCols):

     # 7 loops (as many as the columns)
            #print("b=",b)
            r=a
            c=b
            for bb in range(BoardCols):

                # 7 loops (as many as the columns)
                if r < BoardRows and c < BoardCols:
                    CheckStringDia = CheckStringDia + currentField[r][c]
                    #print(bb)
                    r+=1
                    c+=1

def MakeDiaDownStr():
    global CheckStringDiaDown
    global BoardRows
    global BoardCols
    for a in range(BoardRows):
    # 6 lopps (as many as the rows)
        #print("a=",a)
        for b in range(BoardCols,0,-1):
     # 7 loops (as many as the columns)
            #print("b=",b)
            r=a
            c=b
            for bb in range(BoardCols):
                # 7 loops (as many as the columns)
                if r < BoardRows and 0 <= c < BoardCols:
                    CheckStringDiaDown = CheckStringDiaDown + currentField[r][c]
                    #print(bb)
                    r+=1
                    c-=1

def CheckWinRules():
    #make a string made up with all the horizontal plays
    MakeHorStr()
    #make a string made up with all the horizontal plays
    MakeVerStr()
    MakeDiaStr()
    MakeDiaDownStr()
    CheckWin(CheckStringHor)
    CheckWin(CheckStringVer)
    CheckWin(CheckStringDia)
    CheckWin(CheckStringDiaDown)
    # CheckVer()
    # CheckDia()

# check for 4 consecutive XXXX or OOOO to declare a winner
def CheckWin(CheckString):
    global Result
    if CheckString.find("XXXX") > -1:
        Result = "Player 1 - X WON"
        print(Result)
    elif CheckString.find("OOOO") > -1:
        Result = "Player 2 - O WON"
        print(Result)


while Result =="":
    UserInputCol = int(input("enter col:"))
    # change player and symbol
    FindEmptyRow(UserInputCol,UserSymbol)
    BuildBoard(BoardRows,BoardCols,currentField)
    CheckWinRules()
