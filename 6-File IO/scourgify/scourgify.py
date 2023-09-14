import csv
import sys


def main():
    # Validate the command-line arguments and process the CSV data.
    validation_arg()
    add_row()


def add_row():
    # List to store formatted rows for writing to the output CSV file.
    output = []

    try:
        # Open the input and output CSV files for reading and writing respectively.
        with open(sys.argv[1], "r") as beforeFile, open(sys.argv[2], "w") as afterFile:
            # Read data from the input CSV using DictReader and write formatted data to the output CSV using DictWriter.
            reader = csv.DictReader(beforeFile)
            writer = csv.DictWriter(afterFile, fieldnames=[
                                    "first", "last", "house"])
            writer.writeheader()  # Write header to the output CSV.

            # Process each row in the input CSV, split the name, and format the output data.
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].lstrip(
                ), "last": split_name[0], "house": row["house"]})

            # Write formatted rows to the output CSV.
            for row in output:
                writer.writerow(
                    {"first": row["first"], "last": row["last"], "house": row["house"]})
        return
    except (FileNotFoundError, IndentationError):
        sys.exit(f"Could not read {sys.argv[1]}")


def validation_arg():
    # Check the validity of the command-line arguments.
    length = len(sys.argv)
    if length > 3:
        sys.exit("Too many command-line arguments")
    elif length < 3:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        return


if __name__ == "__main__":
    main()
