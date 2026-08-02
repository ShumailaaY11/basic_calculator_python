# Basic Calculator

A simple console-based calculator built as a Python fundamentals project.
It covers variables, conditionals, loops, functions, dictionaries, and
basic error handling.

## How it works

- A menu lists available operations: add, subtract, multiply, divide,
  power, and modulus.
- You pick an operation and enter two numbers.
- The result is displayed, and the menu loops until you choose to exit.

## Project structure

```
Basic-Calculator/
│
├── main.py         # Menu, user input/output, and error handling
├── calculator.py   # Core math functions + operations dictionary
├── README.md
└── .gitignore
```

## Run it

```bash
python main.py
```

## Concepts practiced

- Variables and data types (`int`, `float`, `str`)
- Conditionals (`if` / `else`)
- Loops (`while`, `for`)
- Functions and dictionaries (mapping menu choices to functions)
- Reading and handling error messages
  (`try` / `except ValueError`, `try` / `except ZeroDivisionError`)

## Possible extensions

- Add a calculation history log
- Support chained operations (e.g., `2 + 3 * 4`)
- Add square root, factorial, or trigonometric functions
