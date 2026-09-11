import { useEffect, useState } from "react";

import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";
import ErrorMessage from "../components/common/ErrorMessage";

import { sendQuestion } from "../services/chatService";

import {
  loadMessages,
  saveMessages,
  clearMessages,
} from "../utils/chatStorage";

function ChatPage() {
  const [messages, setMessages] = useState(() => loadMessages());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    saveMessages(messages);
  }, [messages]);

  const handleNewConversation = () => {
    setMessages([]);
    setError("");
    clearMessages();
  };

  const handleSend = async (question) => {
    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((currentMessages) => [
      ...currentMessages,
      userMessage,
    ]);

    setError("");
    setLoading(true);

    try {
      const data = await sendQuestion(question);

      const assistantMessage = {
        role: "assistant",
        content: data.answer,
        sources: data.sources,
      };

      setMessages((currentMessages) => [
        ...currentMessages,
        assistantMessage,
      ]);
    } catch (error) {
      console.error(
        "Erreur lors de l'appel au backend :",
        error
      );

      setError(
        "Impossible de communiquer avec le serveur. Veuillez réessayer."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <section>
      <div className="d-flex justify-content-between align-items-start mb-4">
        <div>
          <h2 className="h5">
            Comment puis-je vous aider ?
          </h2>

          <p className="text-secondary mb-0">
            Posez une question concernant une démarche administrative.
          </p>
        </div>

        <button
          type="button"
          className="btn btn-outline-secondary btn-sm"
          onClick={handleNewConversation}
          disabled={loading}
        >
          Nouvelle conversation
        </button>
      </div>

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ErrorMessage message={error} />

      <ChatInput
        onSend={handleSend}
        disabled={loading}
      />
    </section>
  );
}

export default ChatPage;