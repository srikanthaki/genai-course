"""
=============================================================
WEEK 2 — SECTION 1: Model Comparison
Compare GPT-4o-mini vs Groq (Llama 3) on the same prompt
=============================================================

What we learn:
- Different models give different answers to the same question
- Response quality, speed, and style vary between providers
- Groq uses the SAME OpenAI SDK — just change base_url and api_key
- This one-line swap pattern is used in real production systems
"""

# --- Step 1: Setup ---
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Loads API keys from your .env file

# --- Step 2: Create TWO clients using the SAME OpenAI library ---
# This is the power of OpenAI-compatible APIs — one SDK, many providers

# Client 1: OpenAI (uses OPENAI_API_KEY from .env)
openai_client = OpenAI()

# Client 2: Groq (FREE! — uses GROQ_API_KEY from .env)
# Only TWO things change: base_url and api_key. Everything else is identical.
groq_client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

# --- Step 3: The SAME prompt for both models ---
PROMPT = "Explain what an API is to a 10-year-old in 3 sentences."

# --- Step 4: Ask GPT-4o-mini ---
print("=" * 60)
print("GPT-4o-mini says:")
print("=" * 60)

gpt_response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": PROMPT}
    ]
)

gpt_answer = gpt_response.choices[0].message.content
print(gpt_answer)

# --- Step 5: Ask Groq (Llama 3 — completely free!) ---
print("\n" + "=" * 60)
print("Groq (Llama 3 70B) says:")
print("=" * 60)

groq_response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # Free model on Groq
    messages=[
        {"role": "user", "content": PROMPT}
    ]
)

groq_answer = groq_response.choices[0].message.content
print(groq_answer)

# --- Step 6: Side-by-side comparison ---
print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)
print(f"GPT-4o-mini length:  {len(gpt_answer)} characters")
print(f"Groq Llama 3 length: {len(groq_answer)} characters")
print()
print("Same question, different answers — that's the nature of LLMs.")
print("Neither is 'right'. They each predicted different probable next tokens.")
print()
print("=" * 60)
print("THE ENGINEERING INSIGHT")
print("=" * 60)
print("""
  Look at the code above. To switch from OpenAI to Groq, we changed:
    1. base_url  (where to send the request)
    2. api_key   (who's paying)
    3. model     (which model to use)
  
  The rest — messages format, response format — is IDENTICAL.
  This is called an "OpenAI-compatible API".
  
  Groq, Together AI, Ollama, and many others follow this pattern.
  Learn the OpenAI SDK once → use it everywhere.
  
  Cost comparison:
    GPT-4o-mini  → paid (cheap, but still costs money)
    Groq Llama 3 → FREE tier available (great for learning!)
""")
