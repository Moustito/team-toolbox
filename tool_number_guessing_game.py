import random

def run():
    goal = random.randint(1, 100)
    left_tries = 7
    print("I'm thinking of a number between 1 and 100.")



    while left_tries > 0:
        user_guess = input("Your guess: ")

        # Check if the input is a valid number
        if not user_guess or not user_guess.isdigit():
            print("Your guess must be a valid number between 1 and 100.")
            continue
        
        # Convert the input to an integer
        user_guess = int(user_guess)

        if user_guess == goal:
            print(f"Well done! You found {goal} in {7 - left_tries} {"attempt" if left_tries == 6 else "attempts"}")
            break
        elif user_guess < 1 or user_guess > 100:
            print("Your guess must be a valid number between 1 and 100.")
        else:
            print(f"{"Too high!" if user_guess > goal else "Too low!"}")

        left_tries -= 1

    if left_tries == 0:
        print(f"Too bad, number I was thinking of was {goal}")


if __name__ == "__main__":
    run()