from voice_input import get_voice_command
from voice_input import get_text_command
from router import route_command
from output import speak
from config import WAKE_WORD

speak("Jarvis online ho gaya bhai")

while True:
    text = get_voice_command()
    if not text:
        text = get_text_command()

    if WAKE_WORD in text:
        text = text.replace(WAKE_WORD, "").strip()

    if not text:
        continue

    response = route_command(text)
    speak(response)
