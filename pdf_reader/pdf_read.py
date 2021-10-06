    """
        Reading PDF Files using pdftotext
        Author: codewith-arijit
        Requirement: https://pypi.org/project/pdftotext/
    """
import pdftotext

# Load your PDF
def view_pdf(filename):
    with open(filename, "rb") as f:
        pdf = pdftotext.PDF(f)

    # If it's password-protected
    #with str many pages?
    #print(len(pdf))

    # Iterate over all the pages
    for page in pdf:
        print(page)

    data = "\n\n".join(pdf)
    # Read all the text into one string
    print(data)

def view_password_protected_pdf(filename):
    
    # If it's password-protected
    with open("secure.pdf", "rb") as f:
        pdf = pdftotext.PDF(f, "secret")

    # How many pages?
    print(len(pdf))

    # Iterate over all the pages
    for page in pdf:
        print(page)

    # Read some individual pages
    print(pdf[0])
    print(pdf[1])

    # Read all the text into one string
    print("\n\n".join(pdf))