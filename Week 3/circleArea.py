# Samat
# 10/10/2026
# Computes the area of a circle from the radius the user enters.

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of a circle with radius", radius, "is", round(area, 2))