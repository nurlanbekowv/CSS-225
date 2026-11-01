# Samat
# 10/31/2026
# Problem 2 - Uses random.randrange to print an odd integer between 0 and 100.

import random

# Start at 1 and step by 2, so only odd numbers (1, 3, 5, ... 99) can be picked
oddNumber = random.randrange(1, 100, 2)
print(oddNumber)
