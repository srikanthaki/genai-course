import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

model = "gpt-4o-mini"

print("="*10)

def bot():
    """Interactive Chat bot with History"""
    system_prompt = "You are a helpful assistant. Keep answers short, concise, and understandable."
    
    history = [
        {"role": "system", "content": system_prompt},
    ]
    print("*"*10)
    print("Simple chat bot with history")
    print("*"*10)
    
    while True:
        user_input = input("\n You:").strip()
        if user_input.lower() == "/quit":
            print("Exiting chat. Goodbye!")
            break
        if not user_input:
            continue
        
        # add user message to history
        history.append({"role": "user", "content": user_input})
        
        # send full history to API
        response = client.chat.completions.create(
            model=model,
            messages=history,
            temperature=0.7,
        )
        
        # Get and print the assistant's response
        assistant_reply = response.choices[0].message.content
        # Add assistant response to history
        history.append({"role": "assistant", "content": assistant_reply})
        print(f"\n Assistant: {assistant_reply}")
        turns = (len(history)-1) // 2
        print(f" [Turn {turns}.length: {len(history)} messages in history]")
        
        
if __name__ == "__main__":
    bot()
        
