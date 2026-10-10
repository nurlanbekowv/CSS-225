# Samat
# 10/10/2026
# Converts degrees Fahrenheit to degrees Celsius.

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, "degrees Fahrenheit is", round(celsius, 2), "degrees Celsius.")