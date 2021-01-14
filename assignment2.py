# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
# in some order, with no integer repeated.

# Your task is to compute the number of inversions in the file given, where the ithi^{th}ith row
# of the file indicates the ithi^{th}ith entry of an array.

# Because of the large size of this array, you should implement the 
# fast divide-and-conquer algorithm covered in the video lectures.

# [TIP: before submitting, first test the correctness of your program on some small test files or your own devising.]

# import integers from ./integerArray.txt


with open("./integerArray.txt") as file:
    lines =[line.rstrip() for line in file]
testArray = [123, 456, 789, 345, 678, 910, 1111, 2211, 212]
counter =0
def countInversions(array1):
    global counter
    if(len(array1) > 1):
        a = array1[:(len(array1) // 2)]
        b = array1[(len(array1) // 2):]
        countInversions(a)
        countInversions(b)
        countA = 0
        countB = 0
        countC = 0
        while countA < len(a) and countB < len(b):
            if a[countA] < b[countB]:
                array1[countC] = a[countA]
                countA = countA+1
            else: 
                array1[countC] = b[countB]
                countB = countB+1
                counter = counter+(len(a)-countA)
            countC = countC+1
            
        while countA < len(a):
            array1[countC]=a[countA]
            countA = countA +1
            countC = countC+1
            
        while countB < len(b):
            array1[countC]=b[countB]
            countB = countB +1
            countC = countC+1
            
#         print('counter: {}'.format(counter))
    return counter
# testArray = [8, 4, 2, 1]
# countInversions(testArray)
countInversions(lines)
