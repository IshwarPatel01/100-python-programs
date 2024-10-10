import math

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b

def get_valid_number(prompt_text):
    while True:
        try:
            num = float(input(prompt_text))
            if math.isfinite(num):  # Check for NaN or Infinity
                return num
            else:
                print("Invalid number (NaN or Infinity). Please try again.")
        except ValueError:
            print("Invalid number. Please try again.")

def get_valid_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input('Enter an Operator (+, -, *, /): ')
        if operator in valid_operators:
            return operator
        print("Invalid operator. Please use one of +, -, *, /.")

def calculator():
    first_number = get_valid_number('Enter First Number: ')
    operator = get_valid_operator()
    second_number = get_valid_number('Enter Second Number: ')

    result = None
    if operator == "+":
        result = sum(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == "/":
        result = divide(first_number, second_number)

    if result is not None:
        print("Result:", result)
    else:
        print("Operation could not be completed due to invalid input.")

# Run the calculator
calculator()
