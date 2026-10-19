# Samat
# 10/18/2026
# Asks for the current time (0-23) and how many hours to wait,
# then prints what time it will be (on a 24-hour clock).

currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print(finalTimeInt)
