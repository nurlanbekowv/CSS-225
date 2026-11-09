# Samat
# 11/9/2026
# CSS 225 - Milestone 3: Trucking Adventure Game
# gameTools.py - Helper functions shared by every chapter.

from random import shuffle

def getChoice(validChoices):
    """Keep asking until the player types one of the valid choices."""
    choice = input("Your choice: ").strip()
    while choice not in validChoices:
        print("That is not a valid choice. Please try again.")
        choice = input("Your choice: ").strip()
    return choice

def showStatus(player):
    """Print the player's money and truck status."""
    print()
    print("---", player["playerName"], "| Money: $" + str(player["money"]),
          "| Fuel:", "Full" if player["hasFuel"] else "Low", "---")

def truckDriver():
    """Create a randomly named truck driver for the player to talk to."""
    driverNames = ["Mike", "Rosa", "Big Tony", "Dana"]
    tips = ["The weigh station in Iowa is open today. Make sure your truck is safe!",
            "A big storm is coming over Nebraska tonight.",
            "Always fuel up before you leave Chicago. Fuel is cheaper here.",
            "Watch your driving hours. The officers check logbooks a lot."]
    # shuffle puts the lists in a random order, then we take the first item
    shuffle(driverNames)
    shuffle(tips)
    driverName = driverNames[0]
    print(driverName + ": Hey there, I'm " + driverName + ". Want to hear a tip?")
    answer = input("Press y to talk to " + driverName + ": ").strip().lower()
    if answer == "y":
        print(driverName + ": " + tips[0])
    else:
        print(driverName + ": Okay, drive safe!")
