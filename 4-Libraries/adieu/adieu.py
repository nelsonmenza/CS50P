import inflect  # Import the inflect library to handle pluralization of words.

p = inflect.engine()  # Create an inflect engine for word pluralization.


def main():
    # Initialize a list with default farewell phrases.
    lst = ["Adieu", "adieu"]
    try:
        while True:
            # Prompt the user to enter a name or input.
            list_input = input("Name: ")
            if list_input == "Liesl":
                # If the input is "Liesl", replace it with "to Liesl".
                list_input = ("to Liesl")

            # Add the input (or modified input) to the list.
            lst.append(list_input)

    # Catch EOFError (usually triggered by Ctrl+D) to stop the loop when the user is done entering names.
    except EOFError:
        if len(lst) == 3:
            # Print farewell message for exactly 3 names.
            print("Adieu, adieu, to Liesl")
        elif len(lst) == 2:
            # Print farewell message for exactly 2 names.
            print("Adieu, adieu, ...")
        elif len(lst) == 4:
            # Print farewell message for exactly 4 names.
            print("Adieu, adieu, to Liesl and Friedrich")

        else:
            # Print farewell message for more than 4 names, using inflect to handle pluralization.
            print(p.join(lst))


# Call the main function to start the process of collecting names and printing farewell messages.
main()
