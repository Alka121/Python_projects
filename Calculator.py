import os

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

operation_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    continue_flag = True  # Define the flag inside the function
    num1 = float(input("Enter the first number: "))  # Use float for consistency

    while continue_flag:
        for symb in operation_dict:
            print(symb)
        
        ope_symb = input("Pick an operation: ")
        if ope_symb not in operation_dict:
            print("Invalid operation! Try again.")
            continue
        
        num2 = float(input("Enter the second number: "))
        
        calculator_function = operation_dict[ope_symb]
        output = calculator_function(num1, num2)
        print(f"{num1} {ope_symb} {num2} = {output}")

        should_continue = input(f"Enter 'y' to continue calculation with {output}, or 'n' to exit: ").lower()
        
        if should_continue == 'y':
            num1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls' if os.name == 'nt' else 'clear')  # Works on Windows & Unix
            print("Calculator exited.")
        else:
            continue_flag = False
            print("Invalid choice. Exiting.")

calculator()