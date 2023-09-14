def main():
    # Prompt user for the current time
    time = input("What time is it? ")
    # Convert the time to a 24-hour format
    hour = convert(time)
    # Check if it's breakfast time
    if hour >= 7.00 and hour <= 8.00:
        print("Breakfast time")
     # Check if it's lunch time
    elif hour >= 12.00 and hour <= 13.00:
        print("Lunch time")
     # Check if it's dinner time
    elif hour >= 18.00 and hour <= 19.00:
        print("Dinner time")


def convert(time):
    # Initialize AM/PM variable
    am_pm = ""
    # Check if the time includes AM/PM
    if len(time) > 5:
        time, am_pm = time.split(" ")
     # Split the time into hour and minutes
    hour, minutes = time.split(":")
    # Convert PM hours to 24-hour format
    if am_pm == "p.m":
        match hour:
            case "1":
                hour = "13"
            case "6":
                hour = "18"
            case "7":
                hour = "19"
     # Convert minutes to decimal format
    minutes = float(minutes) / 60
    # Convert hour to integer and add minutes
    hour = int(hour) + minutes
    # Return the converted hour
    return hour


if __name__ == "__main__":
    main()
