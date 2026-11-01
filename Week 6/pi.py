# Samat
# 10/31/2026
# Problem 4 - Approximates pi with the Leibniz series and compares it to math.pi.
# Leibniz series: pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

import math

numTerms = 100000
piApprox = 0

for term in range(numTerms):
    # Odd denominators 1, 3, 5, 7...; the sign switches between + and -
    piApprox = piApprox + (-1) ** term / (2 * term + 1)

piApprox = piApprox * 4

print("Approximation of pi:", piApprox)
print("math.pi value:      ", math.pi)
