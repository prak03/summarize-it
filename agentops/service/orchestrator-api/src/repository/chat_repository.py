from typing import Optional

from sqlalchemy.orm import Session
from models.chat_model import ChatModel
                                                                                                                                                                                                                                                      
class ChatRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_chat_repo(self, chat: ChatModel):
        self.db.add(chat)        
        self.db.commit()        
        self.db.refresh(chat)
        return chat

    def delete_chat_repo(self, chat_id: str) -> bool:
        chat = self.db.get(ChatModel, chat_id)
        if not chat:
            return False
        self.db.delete(chat)
        self.db.commit()
        return True

    def get_chats_repo(self, chat_id: Optional[str] = None):
        if chat_id:
            chat = self.db.get(ChatModel, chat_id)
            return chat if chat else None                                                                                                                                                                                           
        return self.db.query(ChatModel).all()

    def update_chat_repo(self, chat: ChatModel):
        self.db.commit()
        self.db.refresh(chat)
        return chat