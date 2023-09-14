# Import necessary modules
from datetime import date
import sys
import inflect

# Initialize inflect engine for number-to-words conversion
p = inflect.engine()

# Define a class for date calculation


class DateCalculator():
    """Class for calculating date differences in minutes"""

    def __init__(self, value_date):
        self.value_date = value_date

    def __str__(self):
        # Convert the value_date to words and capitalize the result
        capitalize_value = p.number_to_words(self.value_date, andword="")
        return f"{capitalize_value.capitalize()} minutes"

    def __sub__(self, other):
        # Define subtraction between two DateCalculator instances
        return other.value_date - self.value_date


def main():
    """Main function"""
    delta = get_date()  # Get the difference between birth date and current date
    mint = get_min(delta)  # Convert the difference to minutes
    numbers = DateCalculator(mint)  # Create a DateCalculator instance
    print(numbers)  # Print the formatted result


def get_date():
    """Auxiliary function to get the date difference"""
    current_date = DateCalculator(date.today())  # Get the current date
    try:
        # Get birth date from the user
        birth_day = date.fromisoformat(input("Date of Birth: "))
        # Create a DateCalculator instance for birth date
        born_date = DateCalculator(birth_day)
    except ValueError:
        sys.exit("Invalid date")  # Handle invalid date input
    else:
        delta = born_date - current_date  # Calculate the date difference
    return delta


def get_min(string):
    """Function to convert time difference to minutes"""
    minutes = divmod(string.total_seconds(), 60)
    total_min = minutes[0] + round((minutes[1] / 60))
    return int(total_min)


if __name__ == "__main__":
    main()  # Call the main function to start the program
