"""
Date   : 9/27/2026
Author : samat toktonazarov

"""

# Taking username from user
username = input("Login:  ")

# Declaring users in the system
user1 = "Jack"
user2 = "Jill"

# Comparing input to first variable in database
if username == user1:
    print("Access granted")

# Comparing input to second variable in database
elif username == user2:
    print("Welcome to the system")

# No data was found
else:
    print("Access denied")
