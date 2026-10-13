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