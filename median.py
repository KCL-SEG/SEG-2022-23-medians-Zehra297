"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(numList):
    midVal = len(numList)//2
    numList.sort()
    if len(numList)%2 == 0:
        med = (numList[midVal -1] + numList[midVal])/2
    else:
        med = numList[midVal]
    print(med)
    return med

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

