from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from src.config import settings

DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
