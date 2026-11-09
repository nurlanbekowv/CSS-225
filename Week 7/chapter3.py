# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# chapter3.py - Chapter 3: Nebraska Storm
# Returns the name of the next part of the game.

from gameTools import getChoice, showStatus

def playChapter(player):
    print()
    print("=== CHAPTER 3: NEBRASKA STORM ===")
    print("The sky over Nebraska turned black. The wind pushed the trailer across the lane.")

    while True:
        showStatus(player)
        print("1: Keep driving")
        print("2: Call dispatch")
        print("3: Stop at the rest area and wait")
        print("4: Take a back road shortcut")
        choice = getChoice(["1", "2", "3", "4"])

        if choice == "1":
            print("A strong gust hits the trailer and the truck tips over.")
            return "gameOver"
        elif choice == "2":
            print("Dispatch: There is a rest area 5 miles ahead. Stay safe!")
        elif choice == "3":
            print("You park and wait. By morning the storm is gone.")
            return "chapter4"
        elif choice == "4":
            # The fuel choice from Chapter 1 decides what happens here
            if player["hasFuel"]:
                print("The back road goes nowhere. You get lost and come back to the highway.")
            else:
                print("Your tank runs dry on an empty back road.")
                return "gameOver"
