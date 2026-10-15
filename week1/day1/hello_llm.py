import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_AI_course")
if not api_key:
    raise ValueError(
        "Missing Groq API key. Set GROQ_API_KEY in your environment or .env file."
    )

client = Groq(api_key=api_key)

model = "openai/gpt-oss-20b"
prompt = "Write a short poem about the beauty of nature."
messages = [{"role": "user", "content": prompt}]

response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)



