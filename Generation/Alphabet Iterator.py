import os
import time

if not os.path.exists('data'):
        os.makedirs('data')

def iterate_strings(length):
    count = 1
    prefix = ""
    totalCount = 0
    prevLen = 1
    nextNum = 96
    start = time.perf_counter()
    
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

        if len(array[i]) > prevLen:
            f = open("data/AI_" + str(prevLen) + ".txt", "w+")
            for word in array:
                if word != "" and len(word) == prevLen:
                    f.write(word + "\n")
                    
            f.close()
            finish = time.perf_counter()
            print("\nPrefix: " + str(prefix))
            print("Count: " + str(count))
            print(f"Dumpped length {prevLen} into 'data/AI_" + str(prevLen) + f".txt' in {round(finish-start, 2)} second(s)")
            prevLen += 1

    f = open("data/AI_" + str(prevLen) + ".txt", "w+")
    for word in array:
        if word != "" and len(word) == prevLen:
            f.write(word + "\n")
    f.close()
            
    finish = time.perf_counter()
    print("\nPrefix: " + str(prefix))
    print("Count: " + str(count))
    print(f"Dumpped length {prevLen} into 'data/AI_" + str(prevLen) + f".txt' in {round(finish-start, 2)} second(s)")


def main():
    length = int(input("Max String Length: "))
    print("--------------------")
    iterate_strings(length)
    
main()
