# Samat
# 10/25/2026
# Goes through the numbers 1 to 50. Prints "Divisible by both" for multiples
# of 3 and 5, "Divisible by three" for multiples of 3, "Divisible by five"
# for multiples of 5, and the number itself otherwise.

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)
