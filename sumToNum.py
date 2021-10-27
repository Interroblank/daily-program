# Interroblank, 2020

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# Basic solution.
def sumToNum1(listOfNums, numToFind):

    sumFound = False

    for i in listOfNums:
        for j in listOfNums:
            if i != j and i + j == numToFind:
                sumFound = True

    return sumFound

# Better solution.
def sumToNum2(listOfNums, numToFind):

    sumFound = False
    candidates = []

    for i in listOfNums:
        if i in candidates:
            sumFound = True
        candidates.append(numToFind - i)

    return sumFound
    
