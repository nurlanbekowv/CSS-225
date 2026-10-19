# Module 4 Team Project
# 10/18/2026
# Shows a numbered menu of trucking dispatch options, lets the user pick one,
# and prints a message that includes the value they typed.
# keeps looping until the user chooses 0 (Exit).

userChoice = ""

while userChoice != "0":
    print()
    print("===== Truck Dispatch Menu =====")
    print("1 - Check load status")
    print("2 - Find nearest truck stop")
    print("3 - Log driving hours")
    print("4 - Report a breakdown")
    print("5 - View weather on route")
    print("6 - Contact dispatcher")
    print("0 - Exit")

    userChoice = input("Choose an option (0-6): ")

    if userChoice == "1":
        print("You chose " + userChoice + ": Your load is on time and will be delivered tomorrow.")
    elif userChoice == "2":
        print("You chose " + userChoice + ": The nearest truck stop is 12 miles ahead.")
    elif userChoice == "3":
        print("You chose " + userChoice + ": Your driving hours have been logged.")
    elif userChoice == "4":
        print("You chose " + userChoice + ": Roadside help is on the way.")
    elif userChoice == "5":
        print("You chose " + userChoice + ": Clear skies on your route today.")
    elif userChoice == "6":
        print("You chose " + userChoice + ": Connecting you to the dispatcher...")
    elif userChoice == "0":
        print("You chose " + userChoice + ": Goodbye, drive safe!")
    else:
        print("'" + userChoice + "' is not a valid option. Please try again.")