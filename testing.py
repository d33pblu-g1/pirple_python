dict = {}
dict[1] = 2
dict['1'] = 4
dict[1] += 2
count = 0

for key in dict:
    count += dict[key]

print(count)
