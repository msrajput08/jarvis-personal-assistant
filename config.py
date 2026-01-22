import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API KEYS
OPENAI_KEY = os.getenv("OPENAI_KEY")
GEMINI_KEY = os.getenv("GEMINI_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

print("OPENAI_KEY:", os.getenv("OPENAI_KEY"))
print("GEMINI_KEY:", os.getenv("GEMINI_KEY"))
print("OPENWEATHER_KEY:", os.getenv("OPENWEATHER_KEY"))

# ASSISTANT SETTINGS
WAKE_WORD = "jarvis"
ACTIVE_TIMEOUT = 120  # seconds
