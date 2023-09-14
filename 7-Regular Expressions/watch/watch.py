import re  # Import the 're' module for regular expressions.


def main():
    # Prompt the user for an HTML input and print the parsed YouTube link.
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'<iframe(.)*></iframe>', s):
        # Check if the input contains an iframe tag.
        link_pattern = re.search(
            r'http(s)*:\/\/(www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)', s)
        # Search for a YouTube embed link pattern within the input.
        if link_pattern:
            # Construct the YouTube shareable link using the captured video ID.
            return "https://youtu.be/" + link_pattern.group(3)


if __name__ == "__main__":
    main()  # Call the main function to start the program.
