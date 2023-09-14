def main():
    # Prompt the user to enter the license plate.
    license_plate = input("Enter License Plate: ")
    # Check if the license plate is valid using the is_valid_license_plate function.
    if is_valid(license_plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_length = len(s)  # Get the length of the license plate.
    # Check if the length is between 3 and 6 characters (inclusive).
    if 2 < plate_length < 7:
        # Check the letters in the license plate using the check_letters function.
        has_valid_letters = check_letters(s)
        # Check the numbers in the license plate using the check_numbers function.
        has_valid_numbers = check_numbers(s, plate_length)
        # Combine the results of letter and number checks.
        is_valid = has_valid_letters and has_valid_numbers
        return is_valid  # Return True if both checks passed, otherwise False.
    else:
        return False  # If the length is outside the valid range, return False.


def check_numbers(plate, plate_length):
    # Initialize a variable to store the result of the check for numbers.
    is_valid_numbers = True
    # Define a string containing the valid digits for the license plate.
    valid_digits = "1203456789"
    # Calculate the expected length for the numbers part of the license plate.
    numbers_length = plate_length // 2
    for char in plate:
        if valid_digits.find(char) == numbers_length and plate[round(numbers_length)] == "0":
            # If a zero follows the expected length for numbers, the license plate is invalid.
            return False
        elif valid_digits.find(char) < numbers_length and char in valid_digits:
            # If a digit is found before the expected numbers part, the license plate is invalid.
            is_valid_numbers = False
        else:
            # Otherwise, the digit is valid and the loop continues to check the next character.
            is_valid_numbers = True
    return is_valid_numbers  # Return the result of the check for numbers.


def check_letters(plate):
    # Define a string containing the invalid digits for the letters part of the license plate.
    valid_digits = "1234567890"
    # Define a string containing symbols that are not allowed.
    invalid_symbols = "!@#$%^&*()_+-={}[]|\:;'\<>,.?/~`"
    # Initialize a variable to store the result of the check for letters.
    is_valid_letters = True
    for char in plate:
        if char == " ":
            # If a space is found in the license plate, it is invalid.
            return False
        elif valid_digits.find(plate[0]) != -1 or valid_digits.find(plate[1]) != -1:
            # If the first or second character is a digit, the license plate is invalid.
            return False
        elif invalid_symbols.find(char) != -1:
            # If any symbol is found in the license plate, it is invalid.
            return False
        else:
            # Otherwise, the character is a letter and the loop continues to check the next character.
            is_valid_letters = True
    return is_valid_letters  # Return the result of the check for letters.


if __name__ == "__main__":
    main()  # Call the main function to start the program.
