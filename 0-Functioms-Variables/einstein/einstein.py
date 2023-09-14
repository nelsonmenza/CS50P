# Prompt the user to enter a number
m = int(input("Enter a number: "))
# Define the value of the speed of light
c = 300000000
# Calculate the value of E using the given formula and print the result
E = m * pow(c, 2)
print(f"E = {E:,}")
