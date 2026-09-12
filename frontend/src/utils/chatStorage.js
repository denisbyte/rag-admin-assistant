const STORAGE_KEY = "rag-admin-chat-messages";

export function loadMessages() {
  try {
    const storedMessages = sessionStorage.getItem(STORAGE_KEY);

    if (!storedMessages) {
      return [];
    }

    return JSON.parse(storedMessages);
  } catch (error) {
    console.error(
      "Erreur lors du chargement de la conversation :",
      error
    );

    return [];
  }
}

export function saveMessages(messages) {
  try {
    sessionStorage.setItem(
      STORAGE_KEY,
      JSON.stringify(messages)
    );
  } catch (error) {
    console.error(
      "Erreur lors de la sauvegarde de la conversation :",
      error
    );
  }
}

export function clearMessages() {
  sessionStorage.removeItem(STORAGE_KEY);
}