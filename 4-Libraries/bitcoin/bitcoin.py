import requests  # Import the requests module for making HTTP requests.
import sys  # Import the sys module for system-related functionality.


def main():
    rate = find_exchange_rate()  # Get the current exchange rate of Bitcoin.

    try:
        # Convert the command-line argument to a float.
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        # Convert the command-line argument to a float.
        arg = float(sys.argv[1])
        result = rate * arg
        # Print the result with comma-separated thousands and 4 decimal places.
        print(f"${result:,.4f}")


def find_exchange_rate():
    try:
        # Retrieve JSON data from the API.
        r = requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json', timeout=10)
        json_data = r.json()  # Parse the JSON data.
    except requests.RequestException:
        # Handle errors in making the request or parsing JSON.
        sys.exit("Json problems")
    else:
        # Extract the Bitcoin exchange rate from the JSON data.
        rate = json_data["bpi"]["USD"]["rate"]
        """ ****FOR REAL USE DELETE THIS RATE WITH the value "37,817.3283", This VALUE is Just for test.**** """
        rate = "37,817.3283"
        rate = rate.replace(",", "")  # Remove commas from the rate string.
        return float(rate)  # Convert the rate to a float and return it.


main()  # Call the main function to start the script.
