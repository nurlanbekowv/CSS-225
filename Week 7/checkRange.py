# Samat
# 11/8/2026
# Problem 2 - A function that checks whether a number is in range(1, 10)
# and prints whether it is in or not in the range.

def checkRange(number):
    """Print whether number is in range(1, 10), which means 1 through 9."""
    if number in range(1, 10):
        print(number, "is in the range")
    else:
        print(number, "is not in the range")

userNumber = int(input("Enter a number: "))
checkRange(userNumber)
