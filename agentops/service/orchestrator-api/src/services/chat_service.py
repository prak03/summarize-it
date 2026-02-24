from repository.chat_repository import ChatRepository
import uuid
from datetime import datetime
from models.models import Chat
from typing import Optional

class ChatService: 
    def __init__(self, repo: ChatRepository):
        self.repo = repo

    def create_chat(self, prompt: str):
        print("teesko prompt")
        chat_id = f"id_{uuid.uuid4()}"
        text = (prompt or "").strip()
        now = datetime.utcnow()
        chat = Chat(id=chat_id, created_at=now, updated_at=now, prompt=prompt, messages=[prompt])
        print(vars(chat))
        return self.repo.create_chat_repo(chat, chat_id)

    def get_chats(self, chat_id: Optional[str] = None):
        print("test", chat_id)
        if chat_id:
            return self.repo.get_chats_repo(chat_id)
        return self.repo.get_chats_repo()

    def update_chat(self, chat_id: str, chat: Chat):
        self.chats[chat_id] = chat
        return chat