from dotenv import load_dotenv
load_dotenv()

import os
from google import genai

# Create Gemini client (NEW SDK)
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# Use FREE-TIER SAFE MODEL
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Explain policy memory drift in simple terms"
)

print(response.text)
