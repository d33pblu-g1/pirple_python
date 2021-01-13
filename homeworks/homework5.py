# You're about to do an assignment called "Fizz Buzz", which is one of the
# classic programming challenges. It is a favorite for interviewers, and a
# shocking number of job-applicants can't get it right. But you won't be one of
# those people. Here are the rules for the assignment (as specified by Imran Gory):
#
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number and for the
#  multiples of five print "Buzz".
#
# For numbers which are multiples of both three and five print "FizzBuzz".

# version 1
print("Version 1")

print("1")

for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
         print(str(num)+": FizzBuzz")
    elif num%3 == 0:
         print(str(num)+": Fizz")
    elif num%5 == 0:
         print(str(num)+": Buzz")
    elif num%2 == 0:
         print(str(num)+": is even and therefore not prime")
    else:
        for pnum in range(2,num):
            if pnum == num-1:
                print(str(num)+" is prime")
            elif num%pnum == 0:
                print(str(num) + " can be divided by " + str(pnum) + " therefore it is not prime")
                break
            else:
                continue
print("\n")

# version 2
print("Version 2")
print("1")

for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
         print("FizzBuzz")
    elif num%3 == 0:
         print("Fizz")
    elif num%5 == 0:
         print("Buzz")
    elif num%2 == 0:
         print(num)
    else:
        for pnum in range(2,num):
            if pnum == num-1:
                print("Prime")
            elif num%pnum == 0:
                print(num)
                break
            else:
                continue


#
#
#
# Extra Credit:
#
# Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print
# statement: "prime". You should print this whenever you encounter a number that
# is prime (divisible only by itself and one). As you implement this, don't
# worry about the efficiency of the algorithm you use to check for primes.
# It's okay for it to be slow.
#
