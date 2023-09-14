def main():
    # Prompt user for the cost of the meal and convert it to a float
    dollars = dollars_to_float(input("How much was the meal? "))
    # Prompt user for the tip percentage and convert it to a float
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    # Calculate the tip amount by multiplying the meal cost and tip percentage
    tip = dollars * percent
    # Print the tip amount with 2 decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the dollar sign from the input string
    value = ""
    for i in range(len(d)):
        if d[i] != "$":
            value += d[i]
     # Convert the input string to a float
    return float(value)


def percent_to_float(p):
    # Remove the percentage sign from the input string
    value = ""
    for i in range(len(p)):
        if p[i] != "%":
            value += p[i]
     # Convert the value to a float and divide by 100 to get the decimal representation of the percentage
    result = float(value) / 100
    return result

 # Call the main function to start the program
main()
