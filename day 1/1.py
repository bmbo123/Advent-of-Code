with open('day 1\input.txt','r') as file:
    arr = file.read()

arr  = arr.split("\n")
elf = 0
temp = 0
check = []
for val in arr:
    if val == '':
        check.append(temp)
        if temp > elf:
            elf = temp
        temp = 0
    else:
        temp += int(val)

check.sort()
adds =0
print(check)
print(adds)

print(elf)





