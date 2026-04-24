"""
=============================================================
WEEK 2 — SECTION 2: Tokenization
Count tokens with tiktoken — see why 1 word ≠ 1 token
=============================================================

What we learn:
- Words are split into TOKENS before the model sees them
- 1 word can be 1, 2, or even 3+ tokens
- You pay per token — so this directly affects your bill
- tiktoken is OpenAI's official tokenizer library
"""

import tiktoken

# --- Step 1: Load the tokenizer for GPT-4o / GPT-4o-mini ---
# Different models use different tokenizers
# GPT-4o and GPT-4o-mini both use "o200k_base"
enc = tiktoken.encoding_for_model("gpt-4o-mini")

# --- Step 2: Tokenize a simple sentence ---
text = "I love programming"
tokens = enc.encode(text)

print("=" * 60)
print("TOKENIZATION IN ACTION")
print("=" * 60)
print(f"Text:       '{text}'")
print(f"Token IDs:  {tokens}")
print(f"Num tokens: {len(tokens)}")
print(f"Num words:  {len(text.split())}")
print()

# --- Step 3: See WHAT each token looks like ---
# This is the "aha" moment — students see tokens aren't always words
print("Token breakdown:")
for token_id in tokens:
    # Decode each token back to text
    token_text = enc.decode([token_id])
    print(f"  ID {token_id:>6} → '{token_text}'")

# --- Step 4: Try different texts — see how tokenization varies ---
print("\n" + "=" * 60)
print("DIFFERENT TEXTS, DIFFERENT TOKEN COUNTS")
print("=" * 60)

examples = [
    "Hello",                          # Simple word
    "Hello World",                    # Two simple words
    "Artificial Intelligence",        # Longer words
    "supercalifragilistic",           # Very long word = many tokens
    "123456789",                      # Numbers
    "नमस्ते",                          # Hindi — non-English = more tokens
    "🚀🤖💡",                         # Emojis
    "API_KEY=sk-abc123def456",        # API key pattern
]

for text in examples:
    tokens = enc.encode(text)
    print(f"  '{text}' → {len(tokens)} tokens")

# --- Step 5: The practical rule of thumb ---
print("\n" + "=" * 60)
print("RULE OF THUMB")
print("=" * 60)
long_text = "The quick brown fox jumps over the lazy dog near the riverbank"
tokens = enc.encode(long_text)
words = long_text.split()
ratio = len(tokens) / len(words)
print(f"Text:   '{long_text}'")
print(f"Words:  {len(words)}")
print(f"Tokens: {len(tokens)}")
print(f"Ratio:  {ratio:.2f} tokens per word")
print(f"\nRule of thumb: 1 token ≈ 0.75 words in English")
print(f"Or flip it: 100 words ≈ ~133 tokens")
