length = 0
string="a"
count = 1
nextNum = 96
prefix = ""
totalCount = 0

length = int(input("Max String Length: "))

for i in range(length):
    totalCount += pow(26, i+1)

array = ['' for i in range(totalCount)]

for i in range(0, totalCount):
    nextNum += 1
    if nextNum > 122:
        nextNum = 97
    if i/26 == count:
        prefix = array[count-1]
        count += 1
    array[i] = prefix + chr(nextNum)

print(array)
