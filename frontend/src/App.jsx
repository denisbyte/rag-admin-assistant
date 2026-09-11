import { useState } from "react";

import MainLayout from "./components/layout/MainLayout";
import ChatPage from "./pages/ChatPage";

function App() {
  const [resetChat, setResetChat] = useState(null);

  return (
    <MainLayout onNewConversation={() => resetChat?.()}>
      <ChatPage registerReset={setResetChat} />
    </MainLayout>
  );
}

export default App;