"""
calculator.py

Core arithmetic logic for the Basic Calculator.

Keeping the math functions separate from the input/output loop (in
main.py) makes the code easier to read, test, and debug.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """
    Divide a by b.

    Raises:
        ZeroDivisionError: if b is 0. We let this propagate so the
        caller (main.py) can catch it and show a friendly message,
        which is good practice for reading/debugging error messages.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b


'''Maps menu choice numbers to (label, function) pairs.
Using a dictionary here avoids a long chain of if/elif statements 
in main.py and makes it easy to add new operations later.'''

OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power (a ** b)", power),
    "6": ("Modulus (a % b)", modulus),
}
