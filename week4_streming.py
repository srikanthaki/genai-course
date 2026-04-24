import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

model = "gpt-4o-mini"

print("="*10)

# test_message = [
#     {"role": "system", "content": "You are a helpful assistant. Keep answers short, concise, and understandable."},
#     {"role": "user", "content": "What is Embeddings?"},
# ]

# #normal call
# response = client.chat.completions.create(
#     model=model,
#     messages=test_message,
    
# )


# #streaming call
# stream_response = client.chat.completions.create(
#     model=model,
#     messages=test_message,
#     stream=True
# )

# full_response = ""
# for chunk in stream_response:
#     content = chunk.choices[0].delta.content
#     if content is not None:
#         print(content, end="", flush=True)
#         full_response += content
        

def run_streaming_response():
    """Example of streaming response"""
    system_prompt = "You are a helpful assistant. Keep answers short, concise, and understandable unless asked for more."
    
    history = [
        {"role": "system", "content": system_prompt},
    ]
    
    print("Type /quite to exit.")
    while True:
        user_input = input("\n You:").strip()
        if user_input.lower() == "/quit":
            print("Exiting chat. Goodbye!")
            break
        if not user_input:
            continue
        
        # add user message to history
        history.append({"role": "user", "content": user_input})
        
        # send full history to API with streaming
        stream_response = client.chat.completions.create(
            model=model,
            messages=history,
            temperature=0.7,
            stream=True
        )
        
        
        print(f"\n Assistant: ", end="", flush=True)
        full_response = ""
        for chunk in stream_response:
            content = chunk.choices[0].delta.content
            if content is not None:
                print(content, end="", flush=True)
                full_response += content
        
        print()  # for newline after response is complete
        
        history.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    run_streaming_response()
        


