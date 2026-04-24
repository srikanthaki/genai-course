# WEEK 2 — SECTION 4: Temperature
# See how temperature changes the model's creativity

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

prompt = "Write a one-sentence tagline for a chai shop."

# Temperature 0 — always picks the safest, most probable word
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
)
print("Temp 0:", response.choices[0].message.content)

# Temperature 0.7 — balanced, slight variation each time
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)
print("Temp 0.7:", response.choices[0].message.content)

# Temperature 1.5 — wild, creative, sometimes nonsense
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=1.5,
)
print("Temp 1.5:", response.choices[0].message.content)
