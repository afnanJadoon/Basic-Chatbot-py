import os
import google.generativeai as gemini
from google.generativeai import GenerativeModel
from langgraph.graph import StateGraph,END
from pydantic import BaseModel

gemini.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("gemini-1.5-flash")

class ChatBotState(BaseModel):
    user_input : str
    response : str
    
system_instruction = """You are a helpful AI chatbot.
Your job is to answer questions clearly, politely, and provide explanations when needed.
Always stay on topic and concise in your answers.
"""
    
chat_history = []
    
def chat_bot_node(state : ChatBotState):
    global chat_history
    
    prompt_with_instruction = f"{system_instruction}\nUser: {state.user_input}"
    chat_history.append({"role" : "user", "parts" : [prompt_with_instruction]})
    reply = model.generate_content(chat_history)
    chat_history.append({"role" : "model", "parts" : [reply.text]})
    
    return ChatBotState(user_input = state.user_input, response = reply.text)

graph = StateGraph(ChatBotState)
graph.add_node("gemini",chat_bot_node)
graph.set_entry_point("gemini")
graph.add_edge("gemini",END)

app = graph.compile()

print("\nChatbot is ready! Type 'exit,bye,goodbye' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit","bye","goodbye"]:
        print("Bot: Allah Hafiz.\n")
        break
    
    result = app.invoke(ChatBotState(user_input = user_input, response = ""))
    print("Bot:", result["response"])