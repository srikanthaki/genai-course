# WEEK 2 — SECTION 5: Hallucination
# Catch the LLM confidently making up things that don't exist

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Ask about a completely fake event — watch it make up a detailed answer
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": 
        "Tell me about the Great Pune Earthquake of 1843."
    }],
)
print("FAKE EVENT:", response.choices[0].message.content)
print("\n⚠️  There was NO earthquake in Pune in 1843!\n")

# Ask about a fake research paper — it may summarize a paper that doesn't exist
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": 
        "Summarize the paper 'Neural Pathways in Cloud Formation' by Smith, Nature 2023."
    }],
)
print("FAKE PAPER:", response.choices[0].message.content)
print("\n⚠️  This paper does not exist!")
print("The model predicts PROBABLE text, not TRUE text.")
