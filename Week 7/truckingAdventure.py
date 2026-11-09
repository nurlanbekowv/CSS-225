# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# truckingAdventure.py - The main file. Run this file to play the game.
# It imports each chapter module and calls them in the right order.

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def main():
    print("Welcome to TRUCKING ADVENTURE!")
    playerName = input("What is your name, driver? ").strip()

    # The player dictionary keeps track of everything across the chapters
    player = {
        "playerName": playerName,
        "money": 1500,
        "preTripDone": False,
        "hasFuel": False,
        "cleanInspection": False,
        "calledCustomer": False
    }

    # Each chapter returns where the game goes next
    chapters = {
        "chapter1": chapter1.playChapter,
        "chapter2": chapter2.playChapter,
        "chapter3": chapter3.playChapter,
        "chapter4": chapter4.playChapter,
        "chapter5": chapter5.playChapter
    }

    currentPart = "chapter1"
    while currentPart != "win" and currentPart != "gameOver":
        currentPart = chapters[currentPart](player)

    print()
    if currentPart == "win":
        print("YOU WIN, " + player["playerName"] + "! The load made it to Denver.")
    else:
        print("GAME OVER, " + player["playerName"] + ".")
    print("Final money: $" + str(player["money"]))

main()
