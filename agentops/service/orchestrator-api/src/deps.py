from fastapi import Depends
from repository.chat_repository import ChatRepository
from services.chat_service import ChatService
temp_db = {}

def get_chat_repo() -> ChatRepository:
    return ChatRepository(temp_db)

def get_chat_service(repo: ChatRepository = Depends(get_chat_repo))->ChatService:
    return ChatService(repo)
