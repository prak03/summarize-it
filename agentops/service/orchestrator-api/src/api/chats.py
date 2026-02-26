from fastapi import APIRouter, HTTPException, Depends
from deps import get_chat_service
from services.chat_service import ChatService
from models.models import Chat

router = APIRouter(prefix="/api/chats", tags=["Chats"])

@router.post("/create-chat", response_model=Chat)
def create_chat(prompt: str, chat_service: ChatService = Depends(get_chat_service)):
    return chat_service.create_chat(prompt)

@router.get("/get-chats", response_model=list[Chat])
def get_chats(chat_service: ChatService = Depends(get_chat_service)):
    return chat_service.get_chats()

@router.get("/get-chat/{chat_id}", response_model=Chat | None)
def get_chat(chat_id: str, chat_service: ChatService = Depends(get_chat_service)):
    return chat_service.get_chats(chat_id)

@router.post("/update-chat/{chat_id}", response_model=Chat)
def update_chat(chat_id: str, message: str, chat_service: ChatService = Depends(get_chat_service)):
    updated = chat_service.update_chat(chat_id, message)
    if updated is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return updated

@router.delete("/delete-chat/{chat_id}")
def delete_chat(chat_id: str, chat_service: ChatService = Depends(get_chat_service)):
    if chat_service.delete_chat(chat_id):
        return {"message": "Chat deleted"}
    raise HTTPException(status_code=404, detail="Chat not found")
    