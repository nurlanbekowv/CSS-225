# Samat
# 11/11/2026
# Problem 5 - Uses the character class and a function that checks whether
# the character has all the items needed for a task and no debuff that
# blocks it. Prints the result of each check.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def getNickname(self):
        return self.nickname

    def getWeapons(self):
        return self.weapons

    def getWeaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

def canDoTask(player, taskName, neededItems, blockedDebuffs):
    """Return True if player has every needed item and no blocking debuff."""
    print()
    print("Task:", taskName)
    canDo = True

    # Check every item the task needs
    for item in neededItems:
        if item in player.getWeapons():
            print("  Has", item)
        else:
            print("  Missing", item)
            canDo = False

    # Check every debuff that blocks the task
    for debuff in blockedDebuffs:
        if debuff in player.getWeaknesses():
            print("  Blocked by debuff:", debuff)
            canDo = False
        else:
            print("  Not", debuff)

    if canDo:
        print("  Result:", player.getNickname(), "CAN", taskName.lower())
    else:
        print("  Result:", player.getNickname(), "CANNOT", taskName.lower())
    return canDo

player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

canDoTask(player1, "Climb a mountain", ['rope', 'coat', 'first aid kit'], ['slow'])
canDoTask(player1, "Cook a meal", ['pan', 'groceries'], ['small'])
canDoTask(player1, "Write a book", ['pen', 'paper', 'idea'], ['confusion'])
