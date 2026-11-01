# Samat
# 10/31/2026
# Problem 5 - Converts radians to degrees using the formula
# degrees = radians * 180 / pi, then compares it to math.degrees().

import math

radiansValue = float(input("Enter an angle in radians: "))

degreesValue = radiansValue * 180 / math.pi

print("Calculated degrees:   ", degreesValue)
print("math.degrees() value: ", math.degrees(radiansValue))
