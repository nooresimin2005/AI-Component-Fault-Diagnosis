import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Key loaded:", bool(api_key))

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=30000)
)

print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Reply with only: Gemini connection successful."
)

print("Gemini response:")
print(response.text)