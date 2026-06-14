import os
from groq import Groq
from prompts import SYSTEM_PROMPT

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = []

def get_ai_response(user_text: str) -> str:
    global conversation_history
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_text
    })
    
    # Keep only last 10 messages to save memory
    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]
    
    print(f"👤 User said: {user_text}")
    
    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *conversation_history
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    ai_text = response.choices[0].message.content
    
    # Add AI response to history
    conversation_history.append({
        "role": "assistant",
        "content": ai_text
    })
    
    print(f"🤖 AI response: {ai_text}")
    return ai_text

def reset_conversation():
    global conversation_history
    conversation_history = []