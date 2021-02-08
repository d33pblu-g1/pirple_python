# ParticipantNumber = 5
# ParticipantData = []
# RegisteredParticipants = 0
# OutputFile = open("ParticipantData.txt","w")
#
# while(RegisteredParticipants < ParticipantNumber):
#
#     tempPartData = []
#
#     name = input("please enter your name: ")
#     tempPartData.append(name)
#
#     country = input("please enter your country: ")
#     tempPartData.append(country)
#
#     age = int(input("please enter your age: "))
#     tempPartData.append(age)
#
#     ParticipantData.append(tempPartData)
#
#     RegisteredParticipants += 1
#
# for participant in ParticipantData:
#     for data in participant:
#         OutputFile.write(str(data)) # use string because we cannot write integers
#         OutputFile.write(" ") # put a space after each data
#     OutputFile.write("\n") # add a line at the end of each participant
# OutputFile.close()
#
# print(ParticipantData)

inputFile = open("ParticipantData.txt","r")
inputList = []

for line in inputFile:
    tempParticipant = line.strip("/n").split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(inputList)

Age = {}

for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Countries = {}

for part in inputList:
    tempCountry = part[-2]
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1
print("countries that attended: ", Countries)

Oldest = 0
Youngest = 100
Mode = 0
Counter = 0
for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] >= Counter:
        Counter = Age[tempAge]
        Mode = tempAge

print(Oldest)
print(Youngest)
print("mode :",Mode,"with",Counter,"participants")
inputFile.close()
