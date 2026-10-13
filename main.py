import tool_grades

def show_menu():
    """Display the list of available tools."""
    print()
    print("=== Team Toolbox ===")
    print("3. Grades")
    print("0. Quit")


def main():
    """Ask the user for a choice until they decide to quit."""
    while True:
        show_menu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "3":
            tool_grades.run()
        else:
            print("Invalid choice, try again.")


main()