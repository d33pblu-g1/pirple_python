IsValueAcceptable = False
input1 = ""
#enter Value

# check if integer
while IsValueAcceptable == False:
    input1 = input("enter val")
    try:
        BoardCols  = int(input1)
        IsValueAcceptable = True
    except ValueError:
        print("computer says NO!")
        continue
