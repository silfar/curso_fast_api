from pydantic import BaseSettings

# Classe de configura��o do banco exporta settings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:decastro@localhost:5432/faculdade"
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()
