# Simple calculator program

# Ask the user for the first number
num1_input = input("Enter the first number: ")
# Try to convert it to a float (to allow decimals too)
num1 = float(num1_input)

# Ask the user for the second number
num2_input = input("Enter the second number: ")
num2 = float(num2_input)

# Ask for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Do the math based on the operation entered
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Handle division by zero just in case
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please use +, -, * or /.")
