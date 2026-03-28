import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            return [page.get_text("text") for page in doc]
    except Exception as e:
        raise ValueError(f"Error reading PDF: {e}")

# Extract only name, phone number, and email using field keywords
def extract_focused_fields(text):
    data = {"Name": "N/A", "Phone Number": "N/A", "Email": "N/A"}

    # Name: Full Name or Candidate Name
    name_match = re.search(r"(?:Full Name|Candidate Name):\s*_+(.+?)_+", text)
    if name_match:
        data["Name"] = name_match.group(1).strip()

    # Phone Number: Phone, Cell, Number, etc.
    phone_match = re.search(r"(?:Phone|Phone Number|Cell|Number):\s*_+([\d\-\+\s]+)_+", text)
    if phone_match:
        data["Phone Number"] = phone_match.group(1).strip()

    # Email: Email Address or Email
    email_match = re.search(r"(?:Email|Email Address):\s*_+(.+?)_+", text)
    if email_match:
        data["Email"] = email_match.group(1).strip()

    return data

def process_pdf_and_print_results(pdf_path):
    all_texts = extract_text_from_pdf(pdf_path)
    for idx, text in enumerate(all_texts, start=1):
        result = extract_focused_fields(text)

        # Skip empty or junk pages
        if all(v == "N/A" for v in result.values()):
            continue
        print(f"\nStudent {idx} Information:")
        print(f"Name: {result['Name']}")
        print(f"Phone Number: {result['Phone Number']}")
        print(f"Email: {result['Email']}")

if __name__ == "__main__":

    # For single form sample below
    process_pdf_and_print_results("Registration-Form.pdf")
    
    # For multiple forms sample below
    # process_pdf_and_print_results("multi_registration_forms.pdf")
