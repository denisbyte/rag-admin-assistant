import { useEffect, useRef } from "react";

import ChatMessage from "./ChatMessage";
import SourceList from "./SourceList";
import Loader from "../common/Loader";

import "../../styles/chat.css";

function ChatWindow({ messages, loading }) {
  const bottomRef = useRef(null);

  // Scroll automatique vers le dernier message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  // Aucune conversation
  if (messages.length === 0 && !loading) {
    return (
      <div className="chat-window border rounded-3 bg-light p-4 text-center text-secondary">
        Aucune conversation pour le moment.
      </div>
    );
  }

  return (
    <div className="chat-window border rounded-3 bg-light p-3">
      {messages.map((message, index) => (
        <div key={index}>
          <ChatMessage
            role={message.role}
            content={message.content}
          />

          {message.role === "assistant" && (
            <div className="ms-2 mb-3">
              <SourceList sources={message.sources} />
            </div>
          )}
        </div>
      ))}

      {loading && (
        <div className="ms-2">
          <Loader />
        </div>
      )}

      {/* Point de référence pour l'auto-scroll */}
      <div ref={bottomRef} />
    </div>
  );
}

export default ChatWindow;