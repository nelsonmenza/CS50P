import re
import sys


def main():
    # Get input from user and call the convert function.
    print(convert(input("Hours: ")))


def convert(s):
    try:
        # Check if the input contains a colon to differentiate between cases.
        if ":" in s:
            # Split input into two parts: first and second hours.
            first_hr, second_hr = s.split(" to ")
            # Use regular expressions to find hour and minute information.
            findin_first = re.search(r"(.+\:.+) (AM|PM)", first_hr)
            findin_second = re.search(r"(.+\:.+) (AM|PM)", second_hr)
            hr1, min = findin_first.group(1).split(":")
            hr2, min2 = findin_second.group(1).split(":")
        else:
            # If no colon, assume minutes are 00 and split input.
            min = 00
            min2 = 00
            first_hr, second_hr = s.split(" to ")
            findin_first = re.search(r"(.+) (AM|PM)", first_hr)
            findin_second = re.search(r"(.+) (AM|PM)", second_hr)
            hr1 = findin_first.group(1)
            hr2 = findin_second.group(1)
    except (ValueError, AttributeError):
        raise ValueError

    try:
        # Convert hours and minutes to integers.
        hr1, min = int(hr1), int(min)
        valid_time(hr1, min)
        hr2, min2 = int(hr2), int(min2)
        valid_time(hr2, min2)

        # Handle AM/PM conversion and 24-hour format.
        if (findin_first.group(2) == "PM" and hr1 != 12) or (findin_first.group(2) == "AM" and hr1 == 12):
            if hr1 < 13:
                hr1 = hr1 + 12
            if hr1 == 24:
                hr1 = 00

        if (findin_second.group(2) == "PM" and hr2 != 12) or (findin_second.group(2) == "AM" and hr2 == 12):
            if hr2 < 13:
                hr2 = hr2 + 12
            if hr2 == 24:
                hr2 = 00
    except ValueError:
        raise ValueError

    # Format and return the result.
    return f"{hr1:02d}:{min:02d} to {hr2:02d}:{min2:02d}"


def valid_time(hour, min):
    # Validate the hour and minute values.
    if hour > 12:
        raise ValueError
    if min > 59:
        raise ValueError
    return True


if __name__ == "__main__":
    main()
