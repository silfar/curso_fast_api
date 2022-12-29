from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable = True)
    email = Column(String(100), index=True, nullable = False, unique=True)
    senha = Column(String(256), nullable = False)
    e_admin = Column(Boolean, default=False)
    oss = relationship(
        'OsModel',
        cascade="all,delete-orphan",
        back_populates="analista",
        uselist = True,
        lazy="joined"
        )