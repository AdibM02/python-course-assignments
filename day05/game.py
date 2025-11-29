"""Guessing game module with core logic and game loop."""

import random


def check_guess(guess, target_number):
    """
    Compares the guess to the target number.
    
    Args:
        guess: The player's guessed number
        target_number: The target number to find
        
    Returns:
        "Found" if guess equals target_number
        "Larger" if guess is smaller than target_number
        "Smaller" if guess is larger than target_number
    """
    if guess == target_number:
        return "Found"
    elif guess < target_number:
        return "Larger"
    else:
        return "Smaller"


def run_game():
    """Run the main game loop with user interaction."""
    r = random.randint(1, 100)
    counter = 0
    print("Welcome to the Guessing Game!")
    while True:
        try:
            guess = int(input("Your guess is? "))
            counter += 1
            result = check_guess(guess, r)

            if result == "Found":
                print("You found the number in", counter, "moves.")
                break
            elif result == "Larger":
                print("Larger")
            else:  # "Smaller"
                print("Smaller")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    run_game()
