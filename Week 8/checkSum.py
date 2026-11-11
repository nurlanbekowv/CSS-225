# Samat
# 11/11/2026
# Problem 2 - A function that takes two numbers from the user and prints
# whether their sum is greater than 10, less than 10, or equal to 10.

def checkSum():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    total = firstNumber + secondNumber
    if total > 10:
        print("The sum", total, "is greater than 10")
    elif total < 10:
        print("The sum", total, "is less than 10")
    else:
        print("The sum", total, "is equal to 10")

checkSum()
