import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

_db_path = os.getenv("SQLITE_DB_FILE", "./app.db")
# SQLite URLs need file path; use 3 slashes for absolute path
_db_url = f"sqlite:///{_db_path}" if _db_path.startswith("/") else f"sqlite:///./{_db_path}"

engine = create_engine(
    _db_url,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.create_all(bind=engine)