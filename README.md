# Basic-Chatbot-py  
A simple chatbot built with Google Gemini API, LangGraph, and Pydantic.<br>  
It responds to user input in a conversational style, follows a fixed system instruction and also stores conversation history.<br><br>  

# Gemini Chatbot with LangGraph<br>  
This is a simple chatbot built with Google Gemini API, LangGraph, and Pydantic.<br>  
It takes user input, applies a system instruction for polite and concise answers, sends it to Gemini, and returns a response in a conversational style.<br><br>  

# Features<br>  
- Uses Gemini 1.5 Flash for fast replies<br>  
- Graph-based chatbot flow using LangGraph<br>  
- Clean code structure with Pydantic models<br>  
- Continuous chat loop until you type exit<br>  
- Lightweight and beginner-friendly<br>  
- Stores memory (if you tell it your name and later ask "what is my name?", it will remember)<br><br> 

# Requirements<br>  
Make sure you have:<br>  
- Python 3.9+<br>  
- Google Generative AI SDK (google-generativeai)<br>  
- LangGraph<br>  
- Pydantic<br><br>  

Install dependencies with:<br>  
pip install google-generativeai langgraph pydantic<br><br>  

# Setup<br>  
Get your Gemini API Key from Google AI Studio (https://aistudio.google.com/app/apikey)<br>  
Set it as an environment variable:<br>

Windows (PowerShell):<br>  
setx GEMINI_API_KEY "your_api_key_here"<br><br>   

Mac/Linux (bash/zsh):<br>  
export GEMINI_API_KEY="your_api_key_here"<br><br> 

Clone this repository and run the script:<br>  
python chatbot.py<br><br>  

# Usage<br>  
When you run the program, you’ll see:<br>  
Chatbot is ready! Type 'exit,bye,goodbye' to quit.<br><br> 

Type anything:<br>  
You: Hello bot<br>  
Bot: Hi there! How can I help you today?<br><br>  

Memory example:<br>
You: My name is Afnan<br>
Bot: Nice to meet you, Afnan!<br>
You: What is my name?<br>
Bot: Your name is Afnan.<br><br>

To close the chatbot:<br>  
You: exit<br>  
Bot: Allah Hafiz.<br><br>   

# System Instruction<br>  
By default, the chatbot uses this system instruction:<br>  
You are a helpful AI chatbot.
Your job is to answer questions clearly, politely, and provide explanations when needed.
Always stay on topic and concise in your answers.<br><br>  

You can **change this instruction** in the code to make the chatbot behave differently (e.g., more casual, more detailed, or role-specific).<br><br>  

# Ending Note<br>  
This chatbot ends conversations with "Allah Hafiz". You can change it as you like.<br>
It stores past memory and follows a fixed system instruction to ensure polite and concise answers.<br>
  