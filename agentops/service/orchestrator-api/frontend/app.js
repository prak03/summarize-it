const chatListEl = document.getElementById("chatList");
const chatPlaceholder = document.getElementById("chatPlaceholder");
const chatWindow = document.getElementById("chatWindow");
const chatMessages = document.getElementById("chatMessages");
const chatInputForm = document.getElementById("chatInputForm");
const chatInput = document.getElementById("chatInput");
const btnNewChat = document.getElementById("btnNewChat");

let selectedChatId = null;
let chats = {};

const API = "/api/chats";

async function fetchAllChats() {
  const res = await fetch(API);
  if (!res.ok) throw new Error("Failed to load chats");
  const data = await res.json();
  return typeof data === "object" && data !== null && !Array.isArray(data) ? data : {};
}

async function fetchChat(chatId) {
  const res = await fetch(`${API}/${encodeURIComponent(chatId)}`);
  if (!res.ok) return null;
  return res.json();
}

async function createChat(text) {
  const res = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) throw new Error("Failed to create chat");
  return res.json();
}

async function deleteChat(chatId) {
  const res = await fetch(`${API}/${encodeURIComponent(chatId)}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete chat");
}

function getMessages(chat) {
  if (!chat) return [];
  return Array.isArray(chat) ? chat : (chat.messages || []);
}

function renderChatList() {
  const ids = Object.keys(chats);
  chatListEl.innerHTML = ids.length === 0
    ? "<li class='empty'>No chats yet</li>"
    : ids.map((id) => {
        const messages = getMessages(chats[id]);
        const preview = messages[0] || "New chat";
        const short = preview.length > 42 ? preview.slice(0, 42) + "…" : preview;
        const active = id === selectedChatId ? " active" : "";
        return `<li data-chat-id="${id}" class="chat-item ${active}">
          <span class="chat-item-label">${escapeHtml(short)}</span>
          <button type="button" class="chat-item-delete" title="Delete chat" aria-label="Delete chat">×</button>
        </li>`;
      }).join("");

  chatListEl.querySelectorAll("li.chat-item").forEach((li) => {
    const id = li.dataset.chatId;
    li.querySelector(".chat-item-label").addEventListener("click", () => selectChat(id));
    li.querySelector(".chat-item-delete").addEventListener("click", (e) => {
      e.stopPropagation();
      confirmDelete(id);
    });
  });
}

async function confirmDelete(chatId) {
  if (!confirm("Delete this chat?")) return;
  try {
    await deleteChat(chatId);
    delete chats[chatId];
    if (selectedChatId === chatId) showPlaceholder();
    renderChatList();
  } catch (err) {
    console.error(err);
  }
}

function escapeHtml(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}

function renderChatMessages(messages) {
  const list = Array.isArray(messages) ? messages : [];
  chatMessages.innerHTML = list.map((msg) => `<div class="msg user">${escapeHtml(msg)}</div>`).join("");
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function selectChat(chatId) {
  selectedChatId = chatId;
  chatPlaceholder.classList.add("hidden");
  chatMessages.classList.remove("hidden");
  renderChatList();
  renderChatMessages(getMessages(chats[chatId]));
}

function showPlaceholder() {
  selectedChatId = null;
  chatPlaceholder.classList.remove("hidden");
  chatMessages.classList.add("hidden");
  renderChatList();
}

async function loadChats() {
  try {
    chats = await fetchAllChats();
    renderChatList();
    if (selectedChatId && chats[selectedChatId]) {
      renderChatMessages(getMessages(chats[selectedChatId]));
    }
  } catch (e) {
    console.error(e);
    chatListEl.innerHTML = "<li class='empty'>Error loading chats</li>";
  }
}

chatInputForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = chatInput.value.trim();
  if (!text) return;

  if (!selectedChatId) {
    try {
      const chat = await createChat(text);
      const id = chat.id || chat.chat_id;
      chats[id] = typeof chat.messages !== "undefined" ? chat : { messages: [text] };
      chatInput.value = "";
      selectChat(id);
      renderChatMessages(getMessages(chats[id]));
    } catch (err) {
      console.error(err);
    }
    return;
  }

  const prev = getMessages(chats[selectedChatId]);
  const messages = [...prev, text];
  chats[selectedChatId] = { ...chats[selectedChatId], messages };
  chatInput.value = "";
  renderChatMessages(messages);
});

btnNewChat.addEventListener("click", () => showPlaceholder());

loadChats();
