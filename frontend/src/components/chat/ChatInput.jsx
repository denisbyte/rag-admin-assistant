import { useState } from "react";

function ChatInput({ onSend, disabled = false }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const trimmedQuestion = question.trim();

    if (!trimmedQuestion || disabled) {
      return;
    }

    onSend(trimmedQuestion);
    setQuestion("");
  };

  return (
    <form onSubmit={handleSubmit} className="mt-3">
      <div className="d-flex gap-4">
        <input 
          type="text"
          className="form-control"
          placeholder="Posez votre question..."
          value={question}
          onChange={(event) => setQuestion(event.target.value)}
          disabled={disabled}
        />

        <button
          type="submit"
          className="btn btn-primary"
          disabled={disabled || !question.trim()}
        >
          Envoyer
        </button>
      </div>
    </form>
  );
}

export default ChatInput;