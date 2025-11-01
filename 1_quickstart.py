import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

hackathon_name = os.environ.get("HACKATHON_NAME", "{HACKATHON_NAME}")

response = client.models.generate_content(
    model="gemini-flash-latest", contents=f"When is {hackathon_name}?"
)
print(response.text)