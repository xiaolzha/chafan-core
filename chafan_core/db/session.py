from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chafan_core.app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=settings.DB_SESSION_POOL_SIZE,
    max_overflow=settings.DB_SESSION_POOL_MAX_OVERFLOW_SIZE,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if settings.DATABASE_READ_REPLICA_URL:
    read_engine = create_engine(
        settings.DATABASE_READ_REPLICA_URL,
        pool_pre_ping=True,
        pool_size=settings.READ_DB_SESSION_POOL_SIZE,
        max_overflow=settings.READ_DB_SESSION_POOL_MAX_OVERFLOW_SIZE,
    )
    ReadSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=read_engine)
else:
    read_engine = engine
    ReadSessionLocal = SessionLocal
