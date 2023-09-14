"""
This program takes taco orders from the user, calculates the total receipt, and prints the receipt when the user is done ordering. It supports a predefined taco menu with item names and prices.

Usage:
1. Run the program.
2. Enter taco items from the menu one by one.
3. The program calculates the total receipt, and if the total exceeds $5, it displays the current total.
4. To finish the order, press Ctrl+D (EOF).
5. The program prints the final total receipt.

Example:
Item: Taco
Item: Burrito
Item: Quesadilla
Total: $19.00
Ctrl+D (EOF)

Output:
Total: $19.00
"""


def main():
    # Call the order_tacos function to take the taco order and calculate the total.
    general_order = order_tacos()
    print(general_order)  # Print the total order receipt.


def order_tacos():
    tacos_dict = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    receipt = 0  # Initialize the total receipt value to 0.
    while True:
        try:
            order = input("Item: ")  # Prompt the user to enter the taco item.
            # Add the price of the ordered item to the receipt.
            receipt = receipt + tacos_dict[order.title()]
            if receipt > 5:  # If the receipt total is greater than 5, print the current total.
                print(f"Total: ${receipt:.2f}")
        # Catch EOFError (usually triggered by Ctrl+D) to terminate the loop when the user is done.
        except EOFError:
            # Return the final total receipt as a formatted string.
            return f"Total: ${receipt:.2f}"
        except KeyError:
            # If the user enters an invalid taco item, ignore the KeyError and continue the loop.
            pass


main()  # Call the main function to start the taco ordering process.
