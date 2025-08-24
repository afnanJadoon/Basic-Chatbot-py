import google.generativeai as gemini
from google.generativeai import GenerativeModel
from langgraph.graph import StateGraph,END
from pydantic import BaseModel
import os

gemini.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("gemini-1.5-flash")

class ChatBotState(BaseModel):
    user_input : str
    response : str
    
def chat_bot_node(state : ChatBotState):
    reply = model.generate_content(state.user_input)
    return ChatBotState(user_input = state.user_input, response = reply.text)

graph = StateGraph(ChatBotState)
graph.add_node("gemini",chat_bot_node)
graph.set_entry_point("gemini")
graph.add_edge("gemini",END)

app = graph.compile()

print("\nChatbot is ready! Type 'exit', 'bye', 'goodbye' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit","bye","goodbye"]:
        print("Allah Hafiz.\n")
        break
    
    result = app.invoke(ChatBotState(user_input = user_input, response = ""))
    print("Bot:", result["response"])