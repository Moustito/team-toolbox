'''
It contains at least 2 functions, each with a docstring.
It uses f-strings to display results.

The user guesses until they find it. After each guess, display Too high! or Too low!.
When found, display the number of attempts.
Write at least one function besides run(), for example give_hint(guess, secret) that returns the message.
I'm thinking of a number between 1 and 100.
Your guess: 50
Too high!
Your guess: 25
Too low!
Your guess: 37
Well done! You found 37 in 3 attempts.
⭐ Bonus: limit the game to 7 attempts and reveal the number if the user loses.
'''
import random

def run():
    goal = random.randint(1, 100)
    left_tries = 7
    print("I'm thinking of a number between 1 and 100.")

    while left_tries > 0:
        user_guess = int(input("Your guess: "))

        if user_guess == goal:
            print(f"Well done! You found {goal} in {7 - left_tries} {"attempt" if left_tries == 6 else "attempts"}")
            break
        else:
            print(f"{"Too high!" if user_guess > goal else "Too low!"}")

        left_tries -= 1

    if left_tries == 0:
        print(f"Too bad, number I was thinking of was {goal}")


if __name__ == "__main__":
    run()