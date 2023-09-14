from fpdf import FPDF

class Pdf():
    def __init__(self, name):
        # Initialize the PDF object and set initial configurations.
        self._pdf = FPDF()
        self._pdf.add_page()
        
        # Set font, size, and color for the title.
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align=("c"))
        
        # Add CS50 shirt image.
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        
        # Set font size and color for the text.
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        
        # Add the recipient's name and the course name.
        self._pdf.text(x=60, y=140, txt=f"{name} took CS50")

    def save(self, file_name):
        # Save the PDF to the specified file name.
        self._pdf.output(file_name)

# Get the recipient's name as input.
name = input("Name: ")

# Create a Pdf object, generate the PDF, and save it.
pdf = Pdf(name)
pdf.save("shirtificate.pdf")
