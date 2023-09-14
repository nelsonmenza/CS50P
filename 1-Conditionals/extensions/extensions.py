"""
This program prompts the user to enter a file name, processes the input, and determines the MIME type (content type) based on the file extension. It then prints the corresponding MIME type.

Usage:
1. Run the program.
2. Enter a file name when prompted.
3. The program will check the file extension and print the corresponding MIME type if it recognizes the extension. If the extension is not recognized, it will print "application/octet-stream" as the default MIME type.

Example:
File name: document.pdf
application/pdf
"""
# Prompt the user for the file names
file_name = input("File name: ")
# Remove leading and trailing whitespaces, and convert to lowercase
file_name = file_name.strip().lower()
# Check the file extension and print the corresponding MIME type
if ".jpg" in file_name or ".jpeg" in file_name:
    print("image/jpeg")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".png" in file_name:
    print("image/png")
elif ".zip" in file_name:
    print("application/zip")
elif ".gif" in file_name:
    print("image/gif")
elif ".bin" in file_name:
    print("application/octet-stream")
else:
    print("application/octet-stream")
