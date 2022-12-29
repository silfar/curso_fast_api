from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:decastro@localhost:5432/itadvanced'
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = 'wrz72tGp4_RoyiJe-ppSDO7isn7oDdEgiUp2TC0oYO4'
    """
    
    import secrets
    token = 
    
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()
