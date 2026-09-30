from pypdf import PdfReader


def load_pdf(file):

    documents = []

    reader = PdfReader(file)

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            documents.append({
                "text": text,
                "page": page_number + 1,
                "source": file.name
            })

    return documents