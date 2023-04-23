from math import floor
import random


def guessing_test():
    min = 0
    max = 1000
    secret = random.randrange(max)
    print("Looking for ", secret)

    low_guess = min
    # We add plus 1 due to potentially not getting an even number
    # for the first split
    high_guess = max + 1

    # Divide the range by 2 and make an initial guess
    guess = floor(high_guess / 2)
    print(f"Guessing {guess}")

    if guess < secret:
        # We now know the bottom half of the range
        # does not matter and can ignore it
        low_guess = guess
    elif guess > secret:
        # We now know the upper half of the range
        # does not matter and can ignore it
        high_guess = guess
    elif guess == secret:
        print(f"The number is {guess}... that was easy...")
        return

    while True:
        if high_guess == 1 and high_guess != secret:
            print("Could not guess")
            break
        guess = random.randrange(low_guess, high_guess)
        print(f"Guessing between: {low_guess} | {high_guess}")
        if guess < secret:
            low_guess = guess
        elif guess > secret:
            high_guess = guess
        elif guess == secret:
            print(f"The number is {guess}... that was easy...")
            break


if __name__ == "__main__":
    guessing_test()
