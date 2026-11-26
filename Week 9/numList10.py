# Samat
# 11/25/2026
# Problem 2 - Uses a while loop to build a list L with the numbers 0 to 10.
# Each time through the loop it adds the counter to the list, then adds 1
# to the counter. The loop stops when the counter is greater than 10.

L = []
counter = 0

while counter <= 10:
    L.append(counter)
    counter = counter + 1

print(L)
