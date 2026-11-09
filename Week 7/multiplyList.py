# Samat
# 11/8/2026
# Problem 3 - A function that multiplies all the numbers in a list.
# Uses the list [5, 2, 7, -1].

def multiplyList(numberList):
    """Return the product of all the numbers in numberList."""
    product = 1
    for number in numberList:
        product = product * number
    return product

myList = [5, 2, 7, -1]
print("The product of", myList, "is", multiplyList(myList))
