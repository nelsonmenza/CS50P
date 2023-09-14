"""
This program calculates the energy (E) equivalent of mass (m) using Albert Einstein's famous equation, E=mc^2, where:
- E represents energy in joules,
- m represents mass in kilograms, and
- c represents the speed of light in meters per second (approximately 300,000,000 m/s).

The program prompts the user to input a numerical value for mass (in kilograms) and then calculates the corresponding energy value using the given formula. Finally, it displays the calculated energy value in joules.

Usage:
1. Run the program.
2. Enter the mass in kilograms when prompted.
3. The program will calculate and display the energy equivalent of the provided mass.

Example:
Enter a number: 10
E = 9,000,000,000,000,000 joules
"""

# Prompt the user to enter a number
m = int(input("Enter a number: "))
# Define the value of the speed of light
c = 300000000
# Calculate the value of E using the given formula and print the result
E = m * pow(c, 2)
print(f"E = {E:,}")
