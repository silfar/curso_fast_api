from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session

async def get_session() -> Generator:
    Session: AsyncSession = Session()
    
    try:
        yield Session
    finally:
        await Session.close()