import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()

hackathon_name = os.environ.get("HACKATHON_NAME", "{HACKATHON_NAME}")
reference_url = os.environ.get("REFERENCE_URL", "{REFERENCE_URL}")


tools = [
    types.Tool(url_context=types.UrlContext()),
]

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=f"When is {hackathon_name}? {reference_url}",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
        tools=tools, # Uncomment to pass your tools (defined above) to the config
    ),
)

print(response.text)