import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"At the Bearcats game, a {adjective} {noun} {verb} onto the field and stopped the whole game."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number from 1 to 100: "))
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number.")
            break