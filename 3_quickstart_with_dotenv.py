import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="When is {HACKATHON_NAME}?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
    ),
)
print(response.text)