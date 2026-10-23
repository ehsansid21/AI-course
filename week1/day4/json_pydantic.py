import os

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_AI_course")
if not api_key:
    raise ValueError(
        "Missing Groq API key. Set GROQ_API_KEY in your environment or .env file."
    )

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"
role = "user"


# structure it
class Ticket(BaseModel):
    name: str
    email: str
    issue: str


schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object",
}
system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema. Give me in json format.
{schema}
"""
message_system = {"role": "system", "content": system_prompt}
text = "Hello My name is Ehsan. I have an iphone which stopped working.My address is Bengaluru.My email is abc@gmail.com. My contact number is 90900909."
prompt = f"""
this is a customer ticket. Please extract the personal information from this.
{text}
"""
message = {"role": "user", "content": prompt}
messages = [message_system, message]

response = client.chat.completions.create(
    model=model, messages=messages, response_format=response_format
)
print(response.choices[0].message.content)

############# isko padhte kaise hai
import json
raw_json=response.choices[0].message.content
data_file= json.loads(raw_json)
ticket = Ticket(**data_file)

#
print(ticket.name)
print(ticket.email)
print(ticket.issue)

