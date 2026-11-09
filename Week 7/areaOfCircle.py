# Samat
# 11/8/2026
# Problem 1 - A function areaOfCircle(r) that returns the area of a circle
# with radius r, using math.pi from the math module.

import math

def areaOfCircle(r):
    """Return the area of a circle with radius r."""
    return math.pi * r ** 2

radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is", round(areaOfCircle(radius), 2))