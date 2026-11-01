# Samat
# 10/31/2026
# Problem 6 - Uses a for loop to calculate the factorial of a number
# the user enters, then compares it to math.factorial().

import math

userNumber = int(input("Enter a whole number: "))

factorialResult = 1
for number in range(1, userNumber + 1):
    factorialResult = factorialResult * number

print("Calculated factorial:   ", factorialResult)
print("math.factorial() value: ", math.factorial(userNumber))
