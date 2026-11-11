# Samat
# 11/11/2026
# Problem 4 - A function that takes a year and returns True if it is
# a leap year and False if it is not.
# Rules: divisible by 4 is a leap year, but divisible by 100 is NOT,
# unless it is also divisible by 400.

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

userYear = int(input("Enter a year: "))
print(userYear, "is a leap year:", isLeapYear(userYear))
