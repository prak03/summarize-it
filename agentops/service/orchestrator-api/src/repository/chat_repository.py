from typing import Optional


class ChatRepository:
    def __init__(self, store: dict):
        self.store = store
    def create_chat_repo(self, chat, id):
        self.store[id] = chat
        return chat

    def delete_chat_repo(self, chat_id: str) -> bool:
        if chat_id in self.store:
            del self.store[chat_id]
            return True
        return False

    def get_chats_repo(self, chat_id: Optional[str] = None) -> list:
        if chat_id:
            return [self.store[chat_id]] if chat_id in self.store else []
        return list(self.store.values())