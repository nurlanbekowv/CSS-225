# Samat
# 11/11/2026
# Problem 3 - A function that takes a list and prints whether
# the value 5 is in that list.

def findFive(numberList):
    if 5 in numberList:
        print("5 is in the list", numberList)
    else:
        print("5 is not in the list", numberList)

findFive([1, 3, 5, 7, 9])
findFive([2, 4, 6, 8])
