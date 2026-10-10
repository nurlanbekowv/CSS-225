# Samat
# 10/10/2026
# Computes a car's miles per gallon (MPG).

miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the number of gallons used: "))
mpg = miles / gallons
print("Your car got", round(mpg, 2), "miles per gallon.")