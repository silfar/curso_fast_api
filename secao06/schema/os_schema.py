from typing import Optional
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class OsSchema(BaseModel):
    id_os: Optional[int]
    data_os: datetime
    usuario_id: Optional[int]
    cliente_id: Optional[int]

    class Config:
        orm_mode = True
    