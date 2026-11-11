# Samat
# 11/11/2026
# Problem 1 - A function that takes two inputs from the user
# and prints whether they are equal or not.

def checkEqual():
    firstValue = input("Enter the first value: ")
    secondValue = input("Enter the second value: ")
    if firstValue == secondValue:
        print(firstValue, "and", secondValue, "are equal")
    else:
        print(firstValue, "and", secondValue, "are not equal")

checkEqual()
