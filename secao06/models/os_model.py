from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class OsModel(settings.DBBaseModel):
    __tablename__ = 'os'
    
    id_os = Column(Integer, primary_key = True, autoincrement = True)
    data_os = Column(DateTime, nullable = False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'))
    cliente_id = Column(Integer, ForeignKey('clientes.id_cliente'))
    analista = relationship(
        "UsuarioModel", back_populates='oss', lazy='joined')
    cliente = relationship(
        "ClienteModel", back_populates='clientes', lazy='joined')
    
    