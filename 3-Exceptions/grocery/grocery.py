"""
This program allows the user to create a grocery list by entering items one by one. It counts the occurrences of each item and prints the sorted grocery list in ascending order by item name along with their respective counts.

Usage:
1. Run the program.
2. Enter grocery items one by one. To finish the list, press Ctrl+D (EOF).
3. The program will count the occurrences of each item and print the sorted grocery list.

Example:
Enter grocery items:
Apples
Bananas
Oranges
Apples
Bananas
Ctrl+D (EOF)

Output:
2 Apples
2 Bananas
1 Oranges
"""


def main():
    # Call the grocery_list function to create the grocery dictionary.
    list_grocery = grocery_list()
    # Sort the dictionary by keys in ascending order.
    sorted_dict = dict(sorted(list_grocery.items(), key=lambda item: item[0]))
    for key, value in sorted_dict.items():
        # Print the sorted grocery list with the count and item name.
        print(f"{value} {key}")


def grocery_list():
    # Initialize an empty dictionary to store the grocery items and their counts.
    grocery_dict = {}
    try:
        while True:
            lst_input = input()  # Prompt the user to enter a grocery item.
            # Convert the input to uppercase to make it case-insensitive.
            lst_input = lst_input.upper()
            if lst_input in grocery_dict:
                for key, value in grocery_dict.items():
                    # If the item already exists in the dictionary, increase its count by 1.
                    grocery_dict[lst_input] = value + 1
            else:
                # If the item does not exist in the dictionary, add it with a count of 1.
                grocery_dict[lst_input] = 1

    # Catch EOFError (usually triggered by Ctrl+D) to stop the loop when the user is done entering items.
    except EOFError:
        # Return the final grocery dictionary with item counts.
        return grocery_dict
    except KeyError:
        # If the user enters an invalid item, ignore the KeyError and continue the loop.
        pass


# Call the main function to start the grocery list creation and printing process.
main()
