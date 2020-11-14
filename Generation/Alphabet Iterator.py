import os
import time

length = 0
count = 1
nextNum = 96
prefix = ""
totalCount = 0
prevLen = 1

length = int(input("Max String Length: "))
print("--------------------")

for i in range(length):
    totalCount += pow(26, i+1)
    print(totalCount)
print("Generating Array")
array = ['' for i in range(totalCount)]
print("--------------------")

start = time.perf_counter()
print("Generating Strings")

for i in range(0, totalCount):
    nextNum += 1 
    if nextNum > 122:
        nextNum = 97
    if i/26 == count:
        prefix = array[count-1]
        count += 1
    array[i] = prefix + chr(nextNum)

    if len(array[i]) > prevLen:
        f = open("data/AI_" + str(len(array[i-1])) + ".txt", "w+")
        for word in array:
            if word != "" and len(word) == prevLen:
                f.write(word + "\n")
        f.close()
        finish = time.perf_counter()
        print("\nNextNum: " + str(nextNum))
        print("Prefix: " + str(prefix))
        print("Count: " + str(count))
        print(f"Dumpped length {prevLen} into 'data/AI_" + str(prevLen) + f".txt' in {round(finish-start, 2)} second(s)")
        prevLen += 1
    #print(array[i])

#print(array)

finish = time.perf_counter()
print(f"Dumpped length {str(length)} into 'data/AI_" + str(length) + f".txt' in {round(finish-start, 2)} second(s)")


if not os.path.exists('data'):
    os.makedirs('data')

f = open("data/AI_" + str(length) + ".txt", "w+")

for word in array:
    f.write(word + "\n")

f.close()
