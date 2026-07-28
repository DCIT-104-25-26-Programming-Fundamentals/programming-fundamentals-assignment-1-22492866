# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Returns the quotient of two numbers rounded to 2 decimal places.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of division of two numbers.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


# -----------------------------------------------------------------------------
# MENU AND HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def display_menu():
    """Displays the calculator menu choices."""
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Helper function to prompt and return two floating-point numbers."""
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def format_num(val):
    """Formats float values to display as integers if they are whole numbers."""
    return int(val) if isinstance(val, float) and val.is_integer() else val


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            try:
                num1, num2 = get_numbers()
                n1_fmt, n2_fmt = format_num(num1), format_num(num2)

                if choice == "1":
                    res = add(num1, num2)
                    print(f"Result: {n1_fmt} + {n2_fmt} = {format_num(res)}")

                elif choice == "2":
                    res = subtract(num1, num2)
                    print(f"Result: {n1_fmt} - {n2_fmt} = {format_num(res)}")

                elif choice == "3":
                    res = multiply(num1, num2)
                    print(f"Result: {n1_fmt} * {n2_fmt} = {format_num(res)}")

                elif choice == "4":
                    res = divide(num1, num2)
                    print(f"Result: {n1_fmt} / {n2_fmt} = {res}")

                elif choice == "5":
                    res = modulus(num1, num2)
                    print(f"Result: {n1_fmt} % {n2_fmt} = {format_num(res)}")

                elif choice == "6":
                    res = power(num1, num2)
                    print(f"Result: {n1_fmt} ** {n2_fmt} = {format_num(res)}")

            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Invalid number entered. Please enter numeric values.")
        else:
            print("Error: Invalid option! Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()
