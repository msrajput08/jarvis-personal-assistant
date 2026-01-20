import os

# ================== API KEYS (FROM ENV) ==================

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_KEY_PATH = os.getenv("GEMINI_KEY_PATH")

# ================== ASSISTANT CONFIG ==================

WAKE_WORD = "jarvis"
ACTIVE_TIMEOUT = 30  # seconds
