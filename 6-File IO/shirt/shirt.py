import sys
from PIL import Image, ImageOps


def main():
    # Validate the command-line arguments and process the image.
    validation_arg()
    try:
        imgModif = Image.open(sys.argv[1])  # Open the input image.
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtimg = Image.open("shirt.png")  # Open the shirt image.
    size = shirtimg.size
    # Resize the input image to the size of the shirt image.
    muppet = ImageOps.fit(imgModif, size)
    # Paste the shirt image on top of the resized input image.
    muppet.paste(shirtimg, shirtimg)
    muppet.save(sys.argv[2])  # Save the modified image.


def validation_arg():
    # Check the validity of the command-line arguments.
    extension_list = ["png", "jpg", "jpeg", "webp"]
    # Split the input file name to extract the extension.
    arg1 = sys.argv[1].split(".")
    # Split the output file name to extract the extension.
    arg2 = sys.argv[2].split(".")
    length = len(sys.argv)

    if length > 3:
        sys.exit("Too many command-line arguments")
    elif length < 3:
        sys.exit("Too few command-line arguments")
    elif arg1[1].lower() not in extension_list:
        sys.exit("Invalid input")
    elif arg2[1].lower() not in extension_list:
        sys.exit("Invalid output")
    else:
        if arg1[1].lower() == arg2[1].lower():
            return
        else:
            sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
