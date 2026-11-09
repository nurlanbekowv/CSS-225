# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# chapter2.py - Chapter 2: Iowa Weigh Station
# Returns the name of the next part of the game.

from gameTools import getChoice, showStatus

def playChapter(player):
    print()
    print("=== CHAPTER 2: IOWA WEIGH STATION ===")
    print("Iowa was flat and endless. Then the sign flashed: WEIGH STATION OPEN.")

    showStatus(player)
    print("1: Pull in to the weigh station")
    print("2: Bypass the scale")
    print("3: Turn around")
    choice = getChoice(["1", "2", "3"])

    if choice == "1":
        # The pre-trip inspection from Chapter 1 decides what happens here
        if player["preTripDone"]:
            print("The officer checks your truck. Clean inspection!")
            player["cleanInspection"] = True
            return "chapter3"
        else:
            print("The officer finds a broken light. Your truck is put out of service.")
            print("You have to go back to Chicago and fix it.")
            return "chapter1"
    elif choice == "2":
        print("Lights flash behind you. You are pulled over and fined $1000.")
        player["money"] = player["money"] - 1000
        return "chapter3"
    elif choice == "3":
        print("You turn around and drive back to Chicago.")
        return "chapter1"
