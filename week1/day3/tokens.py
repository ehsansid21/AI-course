
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_AI_course")

if not api_key:
    raise ValueError("Missing Groq API key.")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

role = "user"

prompt1 = "Hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write a 1000 word essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    usage = response.usage

    print(
        f"Prompt: {prompt} --> "
        f"Your tokens: {usage.prompt_tokens}, "
        f"Completion tokens: {usage.completion_tokens}, "
        f"Total tokens: {usage.total_tokens}"
    )
