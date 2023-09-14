"""
This program prompts the user to enter a date in various formats and converts it to a standardized 'yyyy-mm-dd' format. It supports two input date formats: 'mm/dd/yyyy' and 'Month dd, yyyy' (case-insensitive month names with or without a comma after the day). The program validates the date components and handles various error cases.

Usage:
1. Run the program.
2. Enter a date when prompted.
3. The program will convert the date to 'yyyy-mm-dd' format and print it.

Example:
Date: 05/25/2023
2023-05-25

Date: February 14, 2024
2024-02-14
"""


def main():
    # Call the changing_format function to convert the user-entered date to a standardized format.
    date_format = changing_format()
    print(date_format)  # Print the date in the standardized format.


def changing_format():
    month = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ")  # Prompt the user to enter a date.

        if "/" in date:  # Check if the date format is 'mm/dd/yyyy'
            try:
                mm, dd, yyyy = date.split("/")  # Split the date by "/"
                # Convert the date components to integers.
                mm, dd, yyyy = int(mm), int(dd), int(yyyy)
                # Check if the date components are within valid ranges.
                if 0 < mm < 13 and 0 < dd < 32:
                    # Return the date in 'yyyy-mm-dd' format.
                    return "{}-{:0=2d}-{:0=2d}".format(yyyy, mm, dd)
            except ValueError:
                # If there is a ValueError (e.g., non-integer value), ignore the exception and continue the loop.
                pass

        elif ", " in date:  # Check if the date format is 'Month dd, yyyy'
            try:
                # Initialize a variable to store the day component of the date.
                dd = ""
                mm, day, yyyy = date.split(" ")  # Split the date by space.
                if mm in month:  # Check if the month component is a valid month.
                    for n in range(len(day)):
                        if day[n] != ",":
                            # Extract the day component by removing the comma.
                            dd = dd + day[n]
                # Convert the month to its corresponding numeric value.
                mm = int(month.index(mm.capitalize())) + 1
                # Convert the day and year components to integers.
                dd, yyyy = int(dd), int(yyyy)
                # Check if the date components are within valid ranges.
                if 0 < mm < 13 and 0 < dd < 32:
                    # Return the date in 'yyyy-mm-dd' format.
                    return "{}-{:0=2d}-{:0=2d}".format(yyyy, mm, dd)

            except (KeyError, ValueError, IndexError):
                # If there is a KeyError (invalid month), ValueError (non-integer value), or IndexError (missing date component),
                pass
                # ignore the exception and continue the loop.


# Call the main function to start the process of converting and printing the date in the standardized format.
main()
