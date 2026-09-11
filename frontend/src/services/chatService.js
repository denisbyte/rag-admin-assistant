import apiClient from "../api/apiClient";

export async function sendQuestion(question) {
  const response = await apiClient.post("/chat", {
    question,
  });

  return response.data;
}