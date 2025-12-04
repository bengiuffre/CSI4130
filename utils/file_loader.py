import docx
import pdfplumber
import io

def load_file(file):
    """
    Extract text from uploaded resume file.
    Supports PDF, DOCX, and TXT formats.
    Returns extracted text as a string.
    """

    filename = file.filename.lower()

    # Handle PDF files
    if filename.endswith(".pdf"):
        file.seek(0)  # reset pointer
        text = ""
        try:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print("PDF parsing failed:", e)
        return text.strip()

    # Handle DOCX files
    elif filename.endswith(".docx"):
        try:
            file.seek(0)  # reset pointer
            file_bytes = file.read()
            doc = docx.Document(io.BytesIO(file_bytes))
            paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            return "\n".join(paragraphs)
        except Exception as e:
            print("DOCX parsing failed:", e)
            return ""

    # Handle TXT files
    elif filename.endswith(".txt"):
        try:
            file.seek(0)  # reset pointer
            return file.read().decode("utf-8").strip()
        except Exception as e:
            print("TXT decoding failed:", e)
            return ""

    else:
        raise ValueError("Unsupported file format")
