# Samat
# 10/10/2026
# Finds the day of the week you return on (0 = Sunday ... 6 = Saturday)
# from the starting day number and the length of the stay.

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

startDay = int(input("Enter the starting day number (0-6): "))
nights = int(input("Enter the number of nights you will stay: "))

returnDay = (startDay + nights) % 7

print("You will return on", days[returnDay])