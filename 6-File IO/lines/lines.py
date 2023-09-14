import sys


def main():
    # Validate the command-line argument.
    validation = validation_arg()
    # Read lines from the specified file and count non-empty, non-comment lines.
    lines = command_lines()
    print(lines)


def command_lines():
    # Get the path from the command-line argument.
    path = sys.argv[1]
    count_lines = 0
    lines_list = []

    try:
        # Open the file and read lines.
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                lines_list.append(line.strip())
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Count non-empty, non-comment lines.
    for n in lines_list:
        if n.startswith("#"):
            continue
        if n == "":
            continue
        else:
            count_lines += 1
    return count_lines


def validation_arg():
    # Check the validity of the command-line argument.
    length = len(sys.argv)
    if length > 2:
        sys.exit("Too many command-line arguments")
    elif length < 2:
        sys.exit("Too few command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    else:
        return


if __name__ == "__main__":
    main()
