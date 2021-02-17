# Homework Assignment #8: Input and Output (I/O)
# Details:
#
# Create a note-taking program. When a user starts it up, it should prompt them
# for a filename.

import os.path
from os import path

Ufilename = input("Please enter your filename:")
# Ufilename = "asd"
if path.exists(Ufilename) == True:
    # If they enter a file name that already exists, it should ask the user if they want:
    print(Ufilename, "Already exists. Please select one of the following options")
    print("A : to Read the file")
    print("B : to Delete the file and start over")
    print("C : to Append the file")
    print("D : to replace a single line")
    print("-----------------------------------")
    userinput = input()

    # If the user wants to read the file it should simply show the contents of the file on the screen.
    # A) Read the file
    if userinput.upper() == "A":
        print("-----------------------------------")
        ExistingFile = open(Ufilename,"r")

        # for line in ExistingFile:
        #     print(line)
        ExistingContent = ExistingFile.read()
        print(ExistingContent)
        ExistingFile.close()
    # If the user wants to start over then the file should be deleted and another empty one made in its place.
    # B) Delete the file and start over
    elif userinput.upper() == "B":
        ExistingFile = open(Ufilename,"w")
        text2store = input("please enter text to store: ")
        ExistingFile.write(text2store + "\n")
        ExistingFile.close()

    # If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file.
    # C) Append the file
    elif userinput.upper() == "C":
        text2store = input("please enter text to add: ")
        ExistingFile = open(Ufilename,"a")
        ExistingFile.write(text2store + "\n")
        ExistingFile.close()

    # Extra Credit:
    # Allow the user to select a 4th option:
    # D) Replace a single line
    # If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
    # 1) The line number they want to update.
    # 2) The text that should replace that line.
    elif userinput.upper() == "D":
        ExistingFile = open(Ufilename, "r")
        LineCount = 0
        for line in ExistingFile:
             LineCount += 1
             print(LineCount,line,end = "")
        ExistingFile.seek(0)
        LineSelection = int(input("which line would you line to replace?"))
        NewText = input("Enter Text:")
        WholeContent = ExistingFile.readlines()
        WholeContent[LineSelection-1] = NewText + "\n"
        ExistingFile.close()
        ExistingFile = open(Ufilename, "w")
        ExistingFile.writelines(WholeContent)
    else:
        print ("invalid request")
else:
# If they enter a file name that doesn't exist, it should prompt them to enter
# the text they want to write to the file.
    NewFile = open(Ufilename, "w")
# After they enter the text, it should save the file and exit.
    text2store = input("please enter text to store: ")
    NewFile.write(text2store + "\n")
    NewFile.close()
    print("file created")
