# Samat
# 11/25/2026
# Problem 3 - Keeps asking the user for a number, adds each one to a list
# and to a running sum, and stops once the sum is greater than 100.

numberList = []
total = 0

while total <= 100:
    userNumber = float(input("Enter a number: "))
    numberList.append(userNumber)
    total = total + userNumber
    print("Current sum:", total)

print("Numbers entered:", numberList)
print("Final sum:", total, "is greater than 100")
