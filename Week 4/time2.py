# Samat
# 10/18/2026
# Asks what time it is now and how many hours to wait,
# then prints the time the alarm will go off (on a 24-hour clock).

strTime = input("What time is it now? ")
strWaitTime = input("What is the number of hours to wait? ")
time = int(strTime)
waitTime = int(strWaitTime)

timeWhenAlarmGoesOff = (time + waitTime) % 24
print(timeWhenAlarmGoesOff)
