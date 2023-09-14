import re  # Import the 're' module for regular expressions.
import sys  # Import the 'sys' module for system-related operations.


def main():
    # Prompt the user for an IPv4 address and print the validation result.
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        # Use regex to match and capture the four parts of the IP address.
        matches = re.search("^(.+)\.(.+)\.(.+)\.(.+)$", ip)

        if matches:
            num1 = matches.group(1)
            num2 = matches.group(2)
            num3 = matches.group(3)
            num4 = matches.group(4)
            # Check if each part is within valid range.
            if int(num1) > 255 or int(num1) < 0:
                return False
            elif int(num2) > 255 or int(num2) < 0:
                return False
            elif int(num3) > 255 or int(num3) < 0:
                return False
            elif int(num4) > 255 or int(num4) < 0:
                return False
            else:
                return True  # If all parts are valid, return True.
        else:
            return False  # If the regex pattern doesn't match, return False.
    except ValueError:
        # If a ValueError occurs (invalid conversion), return False.
        return False


if __name__ == "__main__":
    main()  # Call the main function to start the program.
