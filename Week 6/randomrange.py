# Samat
# 10/31/2026
# Problem 1 - Uses a for loop and random.randrange to print
# 10 random integers between 25 and 35.

import random

for count in range(10):
    # randrange stops before the end value, so 36 lets 35 be included
    randomNumber = random.randrange(25, 36)
    print(randomNumber)
