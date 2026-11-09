# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# chapter1.py - Chapter 1: Chicago Truck Stop
# Returns the name of the next part of the game.

from gameTools import getChoice, showStatus, truckDriver

def playChapter(player):
    print()
    print("=== CHAPTER 1: CHICAGO TRUCK STOP ===")
    print("The truck stop in Chicago was quiet at 4 a.m.")
    print("Dispatch had one load left, and it had to be in Denver in two days.")

    while True:
        showStatus(player)
        print("1: Talk to other drivers")
        print("2: Do a pre-trip inspection")
        print("3: Fuel up")
        print("4: Leave for Denver")
        choice = getChoice(["1", "2", "3", "4"])

        if choice == "1":
            truckDriver()
        elif choice == "2":
            if player["preTripDone"]:
                print("You already checked the truck. Everything looks good.")
            else:
                print("You find a broken light and fix it. Your truck is safe now.")
                player["preTripDone"] = True
        elif choice == "3":
            if player["hasFuel"]:
                print("Your tank is already full.")
            else:
                player["money"] = player["money"] - 500
                player["hasFuel"] = True
                print("You fill up the tank for $500.")
        elif choice == "4":
            print("You pull out of the truck stop and head west.")
            return "chapter2"
