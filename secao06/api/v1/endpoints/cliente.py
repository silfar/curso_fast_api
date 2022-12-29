from typing import List

from fastapi import APIRouter, status, Depends, HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.cliente_model import ClienteModel
from models.usuario_model import UsuarioModel
from schema.cliente_schema import ClienteSchemaBase
from core.deps import get_session, get_current_user

router = APIRouter()

#POST Cliente
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ClienteSchemaBase)
async def post_cliente(cliente: ClienteSchemaBase, usuario_logado = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    novo_cliente: ClienteModel = ClienteModel(
        nome_fantasia   = cliente.nome_fantasia,
        razao           = cliente.razao,          
        cnpj            = cliente.cnpj,           
        endereco        = cliente.endereco,       
        telefone        = cliente.telefone,       
        nome_contato    = cliente.nome_contato,   
        celular_contato = cliente.celular_contato,        
        email_contato   = cliente.email_contato,  
        cargo_contato   = cliente.cargo_contato,  
        ativo           = cliente.ativo          
    )
    db.add(novo_cliente)
    await db.commit()
    
    return novo_cliente
