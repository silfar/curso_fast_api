from typing import List

from fastapi import APIRouter, status, Depends, HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.os_model import OsModel
from models.usuario_model import UsuarioModel
from schema.os_schema import OsSchema
from core.deps import get_session, get_current_user

router = APIRouter()

#POST OS
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OsSchema)
async def post_os(os: OsSchema, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    nova_os: OsModel = OsModel(
        data_os = os.data_os,
        usuario_id = usuario_logado.id_usuario,
        cliente_id = os.cliente_id
    )
    db.add(nova_os)
    await db.commit()
    
    return nova_os

#GET OS's
@router.get('/', response_model=List[OsSchema])
async def get_oss(db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OsModel)
        result = await session.execute(query)
        oss: List[OsModel] = result.scalars().unique().all()
        
        return oss
    
# GET OS
@router.get('/{os_id}', response_model=OsSchema, status_code=status.HTTP_200_OK)
async def get_os(os_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OsModel).filter(OsModel.id_os == os_id)
        result = await session.execute(query)
        os: OsModel = result.scalars().unique.one_or_none()
        
        if os:
            return os
        else:
            raise HTTPException(detail='OS não encontrada', status_code=status.HTTP_404_NOT_FOUND)
        
# PUT OS
@router.put('/{os_id}', response_model=OsSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_os(os_id: int, os: OsSchema, db:AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(OsModel).filter(OsModel.id_os == os_id).filter(OsModel.usuario_id == usuario_logado.id_usuario)
        result = await session.execute(query)
        os_up: OsModel = result.scalars().unique.one_or_none()
        
        if os_up:
            if os.cliente_id:
                os_up.cliente_id = os.cliente_id
            if os.data_os:
                os_up.data_os = os.data_os
                
            await session.commit()
            
            return os_up
        else:
            raise HTTPException(detail='OS não encontrada', status_code=status.HTTP_404_NOT_FOUND)
        
# DELETE OS
@router.delete('/{os_id}', response_model=OsSchema, status_code=status.HTTP_202_ACCEPTED)
async def delete_os(os_id: int, os: OsSchema, db:AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(OsModel).filter(OsModel.id_os == os_id).filter(OsModel.usuario_id == usuario_logado.id_usuario)
        result = await session.execute(query)
        os_del: OsModel = result.scalars().unique.one_or_none()
        
        if os_del:
            
            await session.delete(os_del)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='OS não encontrada', status_code=status.HTTP_404_NOT_FOUND)