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
