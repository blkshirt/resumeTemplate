from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas("resume.pdf", pagesize=letter)
    width, height = letter

    # Name and Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, height - 72, "Your Name")

    c.setFont("Helvetica", 14)
    c.drawString(72, height - 100, "Your Title")

    # Contact Information
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, height - 140, "Contact Information")
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 160, "Primary Email: your.primary.email@example.com")
    c.drawString(72, height - 180, "Secondary Email: your.secondary.email@example.com")
    c.drawString(72, height - 200, "Phone: (123) 456-7890")

    # Vision
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, height - 240, "My Vision")
    c.setFont("Helvetica", 12)
    vision_lines = [
        "Your vision paragraph line 1.",
        "Your vision paragraph line 2.",
        "Your vision paragraph line 3.",
        "Your vision paragraph line 4.",
        "Your vision paragraph line 5.",
        "Your vision paragraph line 6."
    ]
    y_position = height - 260
    for line in vision_lines:
        c.drawString(72, y_position, line)
        y_position -= 20

    # Education
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y_position - 20, "Education")
    c.setFont("Helvetica", 12)
    y_position -= 40
    c.drawString(72, y_position, "Your Education Entry 1 - Year")
    y_position -= 20
    c.drawString(72, y_position, "Your Education Entry 2 - Year")

    # Experience
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y_position - 40, "Experience")
    c.setFont("Helvetica", 12)
    y_position -= 60
    c.drawString(72, y_position, "Your Job Title at Company Name - Year")
    y_position -= 20
    c.drawString(90, y_position, "- Your first responsibility or achievement.")
    y_position -= 20
    c.drawString(90, y_position, "- Your second responsibility or achievement.")
    y_position -= 20
    c.drawString(90, y_position, "- Your third responsibility or achievement.")
    
    # Add more experience entries as needed
    y_position -= 40

    # Skills
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y_position, "Skills")
    c.setFont("Helvetica", 12)
    y_position -= 20
    c.drawString(90, y_position, "- Skill 1")
    y_position -= 20
    c.drawString(90, y_position, "- Skill 2")
    y_position -= 20
    c.drawString(90, y_position, "- Skill 3")

    # Save the PDF
    c.save()

if __name__ == "__main__":
    create_pdf()
