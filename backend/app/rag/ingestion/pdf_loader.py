"""
 Chargement et extraction du documents PDF
"""
from pathlib import Path
from langchain_core.documents import Document
from pypdf import PdfReader

def load_pdf(file_path: str | Path) -> list[Document]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {path}")
    # Vérifier si le fichier a pour extension pdf
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"le fichier n'est pas un PDF: {path}")
    # Ouverture du document et accès aux pages:
    reader = PdfReader(path)

    documents: list[Document] = []

    for page_number, page in enumerate(reader.pages, start=1):
        # Extraction présent sur la page
        text = page.extract_text() or ""
        # On ignore les pages complètements vides
        if not text.strip():
            continue
        # Création diu document Langchain
        document = Document(
            page_content=text,
            metadata = {
                "document": path.name,
                "page": page_number,
            },
        )

        documents.append(document)
    return documents

def load_documents(directory: str | Path) -> list[Document]:
        # conversion du chemin du répétoire en Path
        directory_path = Path(directory)
        if not directory_path.exists():
            raise FileNotFoundError(
                f"Répetoire introuvale : {directory_path}"
            )
        documents: list[Document] = []

        # Recherche seulement des fichiers PDF présents dans le dossier
        pdf_files = sorted(directory_path.glob("*.pdf"))
        # chargement de chaque PDF et ajoute ses pages à la liste gloable
        for pdf_file in pdf_files:
            documents.extend(load_pdf(pdf_file))

        return documents





