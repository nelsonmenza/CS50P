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
