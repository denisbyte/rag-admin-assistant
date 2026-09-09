from pydantic import BaseModel

class Document(BaseModel):
    """ Informations sur un docuement disponible dans la base documentaire"""
    filename: str
    title: str | None = None
    source: str
    url: str | None = None
    