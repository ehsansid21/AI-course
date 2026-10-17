import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_AI_course")

if not api_key:
    raise ValueError("Missing Groq API key.")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-20b"
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_AI_course")

if not api_key:
    raise ValueError("Missing Groq API key.")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

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


role = "user"
#prompt = "Just Suggest me 5 name for my cloth company and dont me ask me anythng back"
prompt1="Hi"
prompt2="Explain time travel in detail"
prompt3="Write a 1000 word essay on Machine Learning"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role": role,
        "content": prompt
    }
    messages=[message]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    usage = response.usage
    print(f"Prompt: {prompt} --> your tokens : {usage.prompt_tokens}, completion tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens}")
# message_system = [
#     {
#         "role": "system",
#         "content": "You are brand manager who suggests name for my cloth company in one word."
#     }
# ]

# message = [
#     {
#         "role": role,
#         "content": prompt
#     }
# ]

# messagess = message_system + message

# response = client.chat.completions.create(
#     model=model,
#     messages=messagess,
#     temperature=2,
# )

# print(response.choices[0].message.content)