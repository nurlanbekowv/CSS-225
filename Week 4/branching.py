# Samat
# 10/18/2026
# A time traveler has suddenly appeared in your classroom!
# Greets the visitor with a different message if he is from the distant past
# (before 1900), the present era (1900-2020) or the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year < 1900:
    print("Woah, that's the past!")
elif year <= 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")
