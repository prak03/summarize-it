
from fastapi import APIRouter, HTTPException
from models.models import CreateChatBody, UpdateChatBody, Chat
from fastapi import Depends
from deps import get_chat_service
from services.chat_service import ChatService

router = APIRouter(prefix="/api/chats", tags=["Chats"])

@router.post("/create-chat")
def create_chat(prompt: str, chat_service : ChatService = Depends(get_chat_service)):
    return chat_service.create_chat(prompt)

@router.get("/get-chats")
def get_chats(chat_service: ChatService = Depends(get_chat_service)):
    return chat_service.get_chats()

@router.get("/get-chat/{chat_id}")
def get_chat(chat_id: str, chat_service: ChatService = Depends(get_chat_service)):
    c = chat_service.get_chats(chat_id)
    print(c)
    return c


'''
@router.patch("/update-chat/{chat_id}")
def update_chat(chat_id: str, body: UpdateChatBody):
    text = (body.text or "").strip()
    now = datetime.utcnow()
    chat = temp_db.get(chat_id)
    if chat:
        chat.messages.append(text)
        chat.updated_at = now
        return chat
    else:
        raise HTTPException(status_code=404, detail="Chat not found")

@router.delete("/delete-chat/{chat_id}")
def delete_chat(chat_id: str):
    chat = temp_db.get(chat_id)
    if chat:
        del temp_db[chat_id]
        return {"message": "Chat deleted"}
    else:
        raise HTTPException(status_code=404, detail="Chat not found")
'''