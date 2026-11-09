# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# chapter4.py - Chapter 4: Out of Driving Hours
# Returns the name of the next part of the game.

from gameTools import getChoice, showStatus

def playChapter(player):
    print()
    print("=== CHAPTER 4: OUT OF DRIVING HOURS ===")
    print("The storm passed. The clock said 11 hours driven. The logbook was almost full.")
    print("Denver is still 3 hours away.")

    while True:
        showStatus(player)
        print("1: Keep driving over your hours")
        print("2: Call the customer")
        print("3: Take the 10-hour break")
        choice = getChoice(["1", "2", "3"])

        if choice == "1":
            print("An officer checks your logbook at the next stop. You lose your CDL.")
            return "gameOver"
        elif choice == "2":
            if player["calledCustomer"]:
                print("You already called. The customer knows you are coming.")
            else:
                print("The customer says: No problem, we will see you tomorrow morning.")
                player["calledCustomer"] = True
        elif choice == "3":
            print("You sleep at a truck stop and start fresh in the morning.")
            return "chapter5"
