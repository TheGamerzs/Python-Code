import os
import time

if not os.path.exists('data'):
        os.makedirs('data')

global nextNum
global array

nextNum = 96
array = ['' for i in range(135)]

def iterate_strings(length):
    count = 1
    prefix = ""
    totalCount = 0
    prevLen = 1
    
    for i in range(length):
        totalCount += pow(26, i+1)
    
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


def main():
    length = int(input("Max String Length: "))
    print("--------------------")
    iterate_strings(length)
    
main()
