"""
This program prompts the user to enter a mathematical expression in the format 'x operator y', where 'x' and 'z' are integers and 'operator' is one of the four basic arithmetic operators: '+', '-', '*', or '/'. It then calculates and prints the result of the operation.

Usage:
1. Run the program.
2. Enter a mathematical expression when prompted.
3. The program will parse the expression, perform the specified operation, and print the result with one decimal place.

Example:
Expression: 5 + 3
8.0
"""
# Prompt the user to enter an expression
expression = input("Expression: ")
# Split the expression into three parts: x, y, and z
x, y, z = expression.split(" ")
# Convert x and z to integers
x, z = int(x), int(z)
# Perform the operation based on the operator y
if y == "+":
    result = x + z
    print(f"{result:.1f}")
elif y == "-":
    result = x - z
    print(f"{result:.1f}")
elif y == "*":
    result = x * z
    print(f"{result:.1f}")
elif y == "/":
    result = x / z
    print(f"{result:.1f}")
