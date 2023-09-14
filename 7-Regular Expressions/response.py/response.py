from validator_collection import validators, errors  # Import necessary modules


def main():
    # Get user input for email
    email = valid_email(input("What's your email address? "))
    if email == True:
        print("Valid")  # Print "Valid" if email is valid
    else:
        print("Invalid")  # Print "Invalid" if email is not valid


def valid_email(email_input):
    try:
        # Use the validator to check email validity
        email_address = validators.email(email_input)
    except errors.EmptyValueError:
        # Handle the case where the input email is empty
        return False  # Return False since empty emails are invalid
    except errors.InvalidEmailError:
        # Handle the case where the input email is not a valid email format
        return False  # Return False since invalid emails are invalid
    else:
        return True  # Return True if no errors were raised, indicating a valid email


if __name__ == "__main__":
    main()  # Call the main function to start the program
