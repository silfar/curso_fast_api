from typing import Optional

from pydantic import BaseModel, HttpUrl
from schema.os_schema import OsSchema

class ClienteSchemaBase(BaseModel):
    id_cliente: Optional[int] = None
    nome_fantasia: str
    razao: str
    cnpj: str
    endereco: str
    telefone: str
    nome_contato: str
    celular_contato: str
    email_contato: str
    cargo_contato: str
    ativo: bool
    
    class Config:
        otm_mode = True
        
class ClienteSchemaOss(ClienteSchemaBase):
    oss: Optional[List[OsSchema]]