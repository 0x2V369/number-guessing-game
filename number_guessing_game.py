import shutil
import random

SMALLEST_NUMBER_TO_GUESS = 1
LARGEST_NUMBER_TO_GUESS = 100
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 3


def get_difficulty(prompt):
    """Get user selected difficulty."""
    while True:
        difficulty = input(prompt).strip().casefold()
        if difficulty in ['easy', 'hard']:
            return EASY_MODE_ATTEMPTS if difficulty == 'easy' else HARD_MODE_ATTEMPTS
        else:
            print("You must either type 'easy' or 'hard'!")


def get_user_guess(prompt):
    """Get user input as an integer."""
    while True:
        try:
            user_guess = int(input(prompt))
            if SMALLEST_NUMBER_TO_GUESS <= user_guess <= LARGEST_NUMBER_TO_GUESS:
                return user_guess
            else:
                print(f"Please enter an integer between {SMALLEST_NUMBER_TO_GUESS} and {LARGEST_NUMBER_TO_GUESS}.")
        except ValueError:
            print(f"Please enter an integer between {SMALLEST_NUMBER_TO_GUESS} to {LARGEST_NUMBER_TO_GUESS}.")


def clear_screen():
    """Function clears screen when player chooses to play again."""
    print("\n" * shutil.get_terminal_size().lines)


def main():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")

        guesses_left = get_difficulty("Choose a difficulty. Type 'easy' or 'hard': ")
        number_to_guess = random.randint(SMALLEST_NUMBER_TO_GUESS, LARGEST_NUMBER_TO_GUESS)

        while guesses_left > 0:
            print(f"You have {guesses_left} attempts remaining to guess the number.")
            guess = get_user_guess("Make a guess: ")

            if guess > number_to_guess:
                if guess - number_to_guess > 10:
                    print("Way too high!")
                else:
                    print("Too high.")
                guesses_left -= 1
            elif guess < number_to_guess:
                if number_to_guess - guess > 10:
                    print("Way too low!")
                else:
                    print("Too low.")
                guesses_left -= 1
            else:
                print(f"You guessed it! The number was {number_to_guess}")
                break

            if guesses_left == 0:
                print(f"You've run out of guesses. You lose. The number was {number_to_guess}!")
                break

            print("Guess again!")

        to_continue = input("Would you like to play another round? (y/n): ").strip().casefold()
        if to_continue != 'y':
            break
        clear_screen()


if __name__ == '__main__':
    main()
