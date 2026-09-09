"""
 Découpage des documents en chunks
"""
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2500,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(documents)
    return chunks