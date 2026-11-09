# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# chapter5.py - Chapter 5: Denver Warehouse
# Returns the name of the next part of the game.

from gameTools import getChoice, showStatus

def playChapter(player):
    print()
    print("=== CHAPTER 5: DENVER WAREHOUSE ===")
    print("The Denver mountains glowed orange in the morning sun.")
    print("The warehouse gate was finally in sight.")

    while True:
        showStatus(player)
        print("1: Deliver the load")
        print("2: Leave without the signed paperwork")
        print("3: Look for the next load")
        choice = getChoice(["1", "2", "3"])

        if choice == "1":
            # Choices from Chapters 2 and 4 decide the ending
            if player["cleanInspection"] and player["calledCustomer"]:
                print("The customer is happy! You get paid plus a $1000 bonus")
                print("and a new contract for your company.")
                player["money"] = player["money"] + 3000
            else:
                print("The load is delivered and you get paid $2000.")
                player["money"] = player["money"] + 2000
            return "win"
        elif choice == "2":
            print("Without the signed paperwork you cannot get paid.")
            print("You go back to the warehouse to get it signed.")
        elif choice == "3":
            print("You find a new load going back to Chicago and earn $2000.")
            player["money"] = player["money"] + 2000
            # A new trip starts, so the trip checks start over
            player["preTripDone"] = False
            player["hasFuel"] = False
            player["cleanInspection"] = False
            player["calledCustomer"] = False
            return "chapter1"
