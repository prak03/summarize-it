from typing import Optional


class ChatRepository:
    def __init__(self, store: dict):
        self.store = store
    def create_chat_repo(self, chat, id):
        self.store[id] = chat
        print(self.store)

    def get_chats_repo(self, chat_id: Optional[str] = None)->list:
        if chat_id:
            return [self.store[chat_id]]
        print(self.store)
        return list(self.store.values())