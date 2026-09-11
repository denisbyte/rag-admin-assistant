import ReactMarkdown from "react-markdown";

function ChatMessage({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      className={`d-flex mb-3 ${
        isUser ? "justify-content-end" : "justify-content-start"
      }`}
    >
      <div
        className={`p-3 rounded-3 ${
          isUser
            ? "bg-primary text-white"
            : "bg-white border"
        }`}
        style={{ maxWidth: "75%" }}
      >
        <div className="small fw-semibold mb-1">
          {isUser ? "Vous" : "Assistant"}
        </div>

        {isUser ? (
          <div>{content}</div>
        ) : (
         <ReactMarkdown
  components={{
    a: ({ ...props }) => (
      <a
        {...props}
        target="_blank"
        rel="noopener noreferrer"
      />
    ),
  }}
>
  {content}
</ReactMarkdown>
        )}
      </div>
    </div>
  );
}

export default ChatMessage;