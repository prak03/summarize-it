from fastapi import Depends
from repository.chat_repository import ChatRepository
from services.chat_service import ChatService
from sqlalchemy.orm import Session
from db import SessionLocal
from repository.chat_repository import ChatRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_chat_repo(db: Session = Depends(get_db)) -> ChatRepository:
    return ChatRepository(db)

def get_chat_service(repo: ChatRepository = Depends(get_chat_repo))->ChatService:
    return ChatService(repo)
