#!/usr/bin/env python3
import random

secret_number = random.randint(1,10)
attemps = 3
player_won = False

print("I'm thinking of a number between 1 and 10")

while attemps > 0:

    while True:
        guess = input("Take a guess: ")
        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Invalid option!")
    
    
    if guess == secret_number:
        player_won = True
        break
    elif guess < secret_number:
        print("Too low!, Try again.")
    else:
        print("Too high!, Try again")
    attemps -= 1

if player_won == True:
    print("Congratulation!, You guessed the number!")
else:
    print("Sorry, you've run out of attempts. The secret number was: ", secret_number)
