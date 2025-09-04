from pypdf import PdfWriter, PdfReader
import os

path = "pdfs/"
save_path = "merged/"

PDFS_TO_MERGE =["pdf1.pdf", "pdf2.pdf"]
NEW_PDF_NAME = "merged.pdf"

def main():
    writer = PdfWriter()
    for name in PDFS_TO_MERGE:
        for page in PdfReader(os.path.join(path, name)).pages:
            writer.add_page(page)

    with open(os.path.join(save_path, NEW_PDF_NAME), "wb") as f:
        writer.write(f)



if __name__ == "__main__":
    main()
