#!/usr/bin/env python3
# Created by: Vova M
# Created on: November17 2026
# This program asks the user to guess a random number using a while loop and break.

import random


def main():
    # Generate a random number between 0 and 9
    correct_number = random.randint(0, 9)

    # Loop until the user guesses the right number
    while True:
        # Ask the user for their guess
        user_guess_string = input("Guess a number between 0 and 9: ")

        try:
            # Convert the user input to an integer
            user_guess_int = int(user_guess_string)

            # Check if the guess matches the random number
            if user_guess_int == correct_number:
                print("You guessed correctly!")
                break
            else:
                print(f"{user_guess_int} is not the right number. Try again!\n")

        except ValueError:
            # Catch invalid text inputs so the program does not crash
            print(f"{user_guess_string} is not a valid number. Please try again.\n")


if __name__ == "__main__":
    main()
