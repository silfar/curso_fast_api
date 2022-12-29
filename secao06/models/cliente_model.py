from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.configs import settings

class ClienteModel(settings.DBBaseModel):
    __tablename__ = 'clientes'
    
    id_cliente =Column(Integer, primary_key=True , autoincrement=True)
    nome_fantasia = Column(String(256))
    razao = Column(String(256))
    cnpj = Column(String(14))
    endereco = Column(String(256))
    telefone = Column(String(20))
    nome_contato = Column(String(256))
    celular_contato = Column(String(11))
    email_contato = Column(String(100))
    cargo_contato = Column(String(100))
    ativo = True
    oss = relationship(
        'OsModel',
        cascade="all,delete-orphan",
        back_populates="cliente",
        uselist = True,
        lazy="joined"
        )
    
    