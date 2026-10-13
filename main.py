import tool_number_guessing_game

def show_menu():
    """Display the list of available tools."""
    print()
    print("=== Team Toolbox ===")
    print("2. Number Guessing Game")
    print("0. Quit")


def main():
    """Ask the user for a choice until they decide to quit."""
    while True:
        show_menu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Goodbye!")
            break
        if choice == "2":
            tool_number_guessing_game.run()
        else:
            print("Invalid choice, try again.")


main()