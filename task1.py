#! python3

# SD Computing Studies Assignment

import random

def instructions():
    print("\nWelcome to guess the number!\n\nThe game is simple\nThe computer will think of a number between 1 and 100 and you have to try to guess it\nThe computer will tell if your guess is correct, lower or higher than the number the computer is thinking about\nYou get 10 guesses\nAre you ready?")

def game():
    num = int(random.randint(1,100))
    guesses = int(0)
    max_guesses = int(10)

    while max_guesses > guesses:
        guess = int(input("Enter your guess: "))

        if guess >= 100:
            print("Invalid Input\nPlease try again")
            continue
        elif guess <= 0:
            print("Invalid Input\nPlease try again")
            continue
        
        if guess == 87:
            print("You witnessed the bite of 87!\nGame Over!")
            break
        elif guess < num:
            print("Wrong. The number is higher.\nTry again!")
            guesses += 1
            continue
        elif guess > num:
            print("Wrong. The number is lower.\nTry again!")
            guesses += 1
            continue
        elif guess == num:
            print(f"You win! The number was {num} and you guessed it in your {guesses} guess!")
            break 

    if guesses == max_guesses:
        print(f"Game Over! The correct number was {num}")


instructions()
game()

input('\n\nPress ENTER to exit')