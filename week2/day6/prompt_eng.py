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

model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0.9)
    return response.choices[0].message.content

# bad_prompt = """
# This is a user complaint:
# My laptop is not working.
# Classify this
# """

bad_prompt = """
#ROLE:
You are a support assisstant at a mobile/laptop company.
This is a user complaint:
#TASK:
You have to classify issue in a category.
#CONSTRAINT:
You. have to classify issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT:
Your answer should be in word only that belongs to the specified constraint.
#EXAMPLE:
For instance if a user complain says I want a refund then category is return.
#FALLBACK:
if the issue is not related to any of the above categories then you have to say "other".
This is a user complaint:
My marriage is not working.


"""
print(llm_ans(bad_prompt))