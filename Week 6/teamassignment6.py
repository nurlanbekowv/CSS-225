# Abdyrakhman Raiapov, Aman Osmonov, Samat Toktonazarov

import random

play = 'Y'

while play == 'Y':
    number = random.randint(1, 100)

    guess = int(input('Try to guess the number: '))

    if guess == number:
        print('Great! You Won')
    elif guess > number:
        print("It's lower")
        guess = int(input('Try again: '))
        if guess == number:
            print('Great! You Won')
        elif guess > number:
            print("It's lower")
        else:
            print("It's higher")
    else:
        print("It's higher")
        guess = int(input('Try again: '))
        if guess == number:
            print('Great! You Won')
        elif guess > number:
            print("It's lower")
        else:
            print("It's higher")

    play = input('Would you like to guess another number (Y/N)? ')