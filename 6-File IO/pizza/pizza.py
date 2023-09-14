import csv
import sys
from tabulate import tabulate


def main():
    # Validate the command-line argument.
    validation = validation_arg()
    # Format the CSV data and print it using tabulate.
    csv_formatted, header = format_csv()
    print(tabulate(csv_formatted, headers=header[0], tablefmt="grid"))


def format_csv():
    # Get the path from the command-line argument.
    path = sys.argv[1]
    menu_list = []  # List to store the formatted menu data.
    header = []  # List to store the header for tabulate.

    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            # Determine the header based on the file type (regular or sicilian).
            if "regular" in path:
                header.append({"Regular Pizza": "Regular Pizza",
                              "Small": "Small", "Large": "Large"})
            else:
                header.append({"Sicilian Pizza": "Sicilian Pizza",
                              "Small": "Small", "Large": "Large"})

            # Iterate through the CSV data and format it for tabulate.
            for row in reader:
                if "regular" in path:
                    menu_list.append(
                        {"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
                else:
                    menu_list.append(
                        {"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})

        return menu_list, header
    except FileNotFoundError:
        sys.exit("File does not exist")


def validation_arg():
    # Check the validity of the command-line argument.
    length = len(sys.argv)
    if length > 2:
        sys.exit("Too many command-line arguments")
    elif length < 2:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return


if __name__ == "__main__":
    main()
