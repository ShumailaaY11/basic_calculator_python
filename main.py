"""
main.py

Entry point for the Basic Calculator.

Run this file to start:
    python main.py

This file handles the menu, user input, and error handling.
The actual math lives in calculator.py.
"""

from calculator import OPERATIONS


def print_menu():
    print("\n" + "=" * 40)
    print(" BASIC CALCULATOR")
    print("=" * 40)
    for key, (label, _) in OPERATIONS.items():
        print(f"  {key}. {label}")
    print("  0. Exit")
    print("-" * 40)


def get_number(prompt):
    """
    Keep asking until the user enters a valid number (int or float).
    Demonstrates catching and handling a ValueError instead of
    crashing the program.
    """
    while True:
        raw_input_value = input(prompt)
        try:
            return float(raw_input_value)
        except ValueError:
            print(f"'{raw_input_value}' is not a valid number. Please try again.")


def format_result(value):
    """Show whole numbers without a trailing '.0' for a cleaner look."""
    if value == int(value):
        return str(int(value))
    return str(value)


def main():
    while True:
        print_menu()
        choice = input("Choose an operation: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print(f"'{choice}' is not a valid option. Please choose again.")
            continue

        label, operation_func = OPERATIONS[choice]

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = operation_func(num1, num2)
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            continue

        print(f"\nResult: {format_result(num1)} {label.lower()} {format_result(num2)} = {format_result(result)}")


if __name__ == "__main__":
    main()
