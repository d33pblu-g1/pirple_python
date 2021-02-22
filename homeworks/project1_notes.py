


rows = 6
cols = 7

B = 0

for q in range(rows):
    print("break: q=",q)
    #print("here1")
    a = q
    for i in range(cols):
        print("here2 i=",i)
    #range(start,stop,step)

        b = B
        print("here3 a=",a)
        for w in range(cols):
            if b < cols and a < rows:
                print(a,b)
                a += 1
                b += 1
            else:
                print("here 4")
                b = 0
                break
            B += 1
            #print("B",B)

    B = 0
    b = 0
