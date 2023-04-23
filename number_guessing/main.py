import random

# Max number player can guess 0 to MAX
MAX: int = 100

# Difficulty Modifiers
NORMAL: int = 15
MEDIUM: int = 10
HARD: int = 5


def get_difficulty() -> int:
    """Ask user what difficulty they want and return the number of tries they
    will get.

    Return:
        int - Number of tries the user gets
    """
    # Keep looping until the user picks a proper value
    while True:
        print("Select Difficulty:")
        print(f"\t1 - Normal ({NORMAL})")
        print(f"\t2 - Medium ({MEDIUM})")
        print(f"\t3 - Hard ({HARD})")
        difficulty = input("Select Difficulty: ")

        # Attempt to cast the users string to an int
        try:
            difficulty = int(difficulty)
        # Provide user an error message and continue to next loop so program
        # does not crash if they enter something invalid
        except ValueError:
            print("You must enter a difficult. (1, 2, or 3)")
            continue

        # Assign correct number of guesses based on difficulty
        if difficulty == 1:
            print("Selected: Normal")
            return NORMAL
        elif difficulty == 2:
            print("Selected: Medium")
            return MEDIUM
        elif difficulty == 3:
            print("Selected: Hard")
            return HARD
        else:
            # Should never run
            return NORMAL


def generate_number() -> int:
    """Return a number between 0 and max"""
    return random.randrange(MAX)


def guessing_loop(guesses_remaining: int, secret: int):
    """Make player guess until out of guesses
    or they get the correct answer."""
    # While the player has guesses
    while guesses_remaining > 0:
        # Have the player input a guess and give them a hint
        # for how high the number can go
        guess = input(f"Guess (0 - {MAX}): ")
        # Convert guess to int
        try:
            guess = int(guess)
        except ValueError:
            # Could not convert string to int error and start next loop
            print(f"You must enter a whole number between 0 and {MAX}")
            continue
        if guess == secret:
            print("You win! Congrats!")
            break
        elif guess > secret:
            print("Too high try again!")
        elif guess < secret:
            print("Too low try again!")
        else:
            # This should never run
            print("Incorrect! Try again!")

        # Take away a guess from the player
        guesses_remaining -= 1
    print("Out of guesses... better luck next time!")


if __name__ == "__main__":
    # Get amount of guesses by difficulty
    max_guesses = get_difficulty()
    # Create a secret number to guess
    secret_number = generate_number()
    # Start main game loop
    guessing_loop(max_guesses, secret_number)
