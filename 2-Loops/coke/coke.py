
"""
This program simulates a vending machine's coin operation. It continuously prompts the user to insert coins until the amount due becomes zero or negative, and it keeps track of the change owed or additional amount due.

Usage:
1. Run the program.
2. The initial amount due is set to $50.
3. Insert coins (25 cents, 10 cents, or 5 cents) when prompted.
4. The program deducts the appropriate amount for each coin inserted and checks the updated amount due.
5. When the amount due becomes zero or negative, it prints the change owed to the user.

Example:
Amount Due: 50
Insert coin:25
Amount Due: 25
Insert coin:10
Amount Due: 15
Insert coin:5
Amount Due: 10
Insert coin:25
Amount Due: 10
Insert coin:10
Amount Due: 0
Change Owed: 10
"""


def main():
    amount_due = 50
    print("Amount Due:", amount_due)  # Print the initial amount due.

    # Keep requesting coins until the amount_due becomes zero or negative.
    while amount_due > 0:
        coin = int(input("Insert coin:"))  # Prompt the user to insert a coin.

        # Check the value of the coin and deduct the appropriate amount from amount_due.
        if coin == 25:
            amount_due -= 25
        elif coin == 10:
            amount_due -= 10
        elif coin == 5:
            amount_due -= 5

        # After each coin is inserted, check the updated amount_due status.
        amount_due_check(amount_due)


def amount_due_check(amount):
    # If the amount is less than or equal to zero, the change is owed to the user.
    if amount <= 0:
        print("Change Owed:", abs(amount))
    else:
        # If the amount is still positive, there is more amount due to be paid.
        print("Amount Due:", amount)


if __name__ == "__main__":
    main()
