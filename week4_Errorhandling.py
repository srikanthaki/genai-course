import os
import time
from dotenv import load_dotenv
from openai import (OpenAI,AuthenticationError,RateLimitError,APITimeoutError,APIConnectionError,BadRequestError)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4o-mini"



def safe_api_call(messages,maxretries=3):
    """API call with error handling and retry logic"""
    """Function to demonstrate error handling for API calls"""
    for attempt in range(1, maxretries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
            )
            return{
                "content": response.choices[0].message.content,
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            }
        except AuthenticationError as e:
            print(f"Authentication Error: {e}. Please check your API key.")
            return None
        except BadRequestError  as  b:
            print(f"Bad Request Error: {b}. Please check your request parameters.")
            return None
        except RateLimitError as r:
            wait_time = 5 * attempt  # Exponential backoff
            print(f"\n rate limited.retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except APITimeoutError as t:
            print(f"Timeout Error: {t}. Retrying...")
            time.sleep(2)
        except APIConnectionError as a:
            print(f"Connection Error: {a}. Retrying...")
            time.sleep(2)
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Retrying...")
            return None
    print("Max retries reached. Please try again later.")
    return None

class Costtraker:
    """Class to track API usage and costs"""
    def __init__(self):
        self.total_input = 0
        self.total_output = 0
        self.total_calls = 0.0
    def add_usage(self,prompt_tokens,completion_tokens):
        self.total_input += prompt_tokens
        self.total_output += completion_tokens
        self.total_calls += 1
    def get_cost(self):
        # Example cost calculation based on hypothetical pricing
        cost_per_1k_input = 0.001  # $0.001 per 1000 input tokens
        cost_per_1k_output = 0.002  # $0.002 per 1000 output tokens
        total_cost = (self.total_input / 1000) * cost_per_1k_input + (self.total_output / 1000) * cost_per_1k_output
        return total_cost
def run_chatbot():
    history = [
        {"role": "system", "content": "You are a helpful assistant. Keep answers short, concise, and understandable."},
    ]
    tracker = Costtraker()
    print("Chatbot with error handling and cost tracking.")
    print("/cost to view total cost. /quit to exit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "/quit":
            print("Exiting chat. Goodbye!")
            break
        if user_input.lower() == "/cost":
            print(f"Total API calls: {tracker.total_calls}, Total cost: ${tracker.get_cost():.4f}")
            continue
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        result = safe_api_call(history)
        if result is None:
            continue

        assistant_reply = result["content"]
        tracker.add_usage(result["prompt_tokens"], result["completion_tokens"])
        history.append({"role": "assistant", "content": assistant_reply})
        print(f"\nAssistant: {assistant_reply}")

if __name__ == "__main__":
    run_chatbot()