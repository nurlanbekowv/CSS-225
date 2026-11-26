# Samat
# 11/25/2026
# Problem 4 - A while loop that counts from 0 to 50. If the counter is
# divisible by 10, it is added to the list called tens.

tens = []
counter = 0

while counter <= 50:
    # % 10 == 0 means there is no remainder, so it divides evenly by 10
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print("Numbers divisible by 10:", tens)
