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
