# | | 0
#----- 1
# | | 2
#----- 3
# | | 4


def drawField(field):
    for row in range(5):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(5):
                practicalColumn = int(column/2)
                if column == 4:
                    print(field[practicalColumn][practicalRow])
                elif column%2 == 0:
                    print(field[practicalColumn][practicalRow], end="")
                else:
                    print("|", end = "")
        else:
            print("-"*5)

Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]

print(currentField)
while (True):
    print("Player:",Player)
    MoveRow = int(input("Enter row: \n"))-1
    MoveCol = int(input("Enter column: \n"))-1
    if Player == 1:
        # make move for Player 1
        if currentField[MoveCol][MoveRow] == " ":
            currentField[MoveCol][MoveRow] = "X"
            Player = 2
    else:
        # make move for Player 2
        if currentField[MoveCol][MoveRow] == " ":
            currentField[MoveCol][MoveRow] = "O"
            Player = 1
    #print(currentField)
    drawField(currentField)
