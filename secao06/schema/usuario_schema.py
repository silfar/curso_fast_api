from typing import Optional, List
from pydantic import BaseModel, EmailStr

from schema.os_schema import OsSchema

class UsuarioSchemaBase(BaseModel):
    id_usuario: Optional[int] = None
    nome: str
    sobrenome: str
    email: str
    e_admin: bool = False
    
    class Config:
        orm_mode = True
        
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
class UsuarioSchemaOss(UsuarioSchemaBase):
    oss: Optional[List[OsSchema]]
    
class UsuarioSchemaUP(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    e_admin: Optional[bool]