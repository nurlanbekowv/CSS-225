# Samat
# 11/8/2026
# Problem 4 - A function that takes a list of numbers and returns a new list
# with only the unique elements, using append. Uses [1, 3, 3, 3, 6, 2, 3, 5].

def uniqueList(numberList):
    """Return a new list with each number from numberList only once."""
    uniqueNumbers = []
    for number in numberList:
        # Only add the number if it is not already in the new list
        if number not in uniqueNumbers:
            uniqueNumbers.append(number)
    return uniqueNumbers

myList = [1, 3, 3, 3, 6, 2, 3, 5]
print("Original list:", myList)
print("Unique list:  ", uniqueList(myList))
