import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()

hackathon_name = os.environ.get("HACKATHON_NAME", "{HACKATHON_NAME}")

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=f"When is {hackathon_name}?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)