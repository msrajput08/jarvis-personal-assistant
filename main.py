import time
from voice_input import get_voice_command, get_text_command
from router import route_command
from output import speak, speaking
from config import WAKE_WORD

ACTIVE_TIMEOUT = 120

speak("Jarvis online ho gaya bhai 👋")

active = False
last_active_time = 0

while True:
    if speaking():
        time.sleep(0.1)
        continue

    text = get_voice_command()
    if not text:
        text = get_text_command()

    if not text:
        continue

    text = text.lower().strip()
    print("DEBUG INPUT:", text)

    if WAKE_WORD in text:
        active = True
        last_active_time = time.time()
        text = text.replace(WAKE_WORD, "").strip()

        if not text:
            speak("Haan bhai, bol 😎")
            continue

    if not active:
        continue

    if time.time() - last_active_time > ACTIVE_TIMEOUT:
        speak("Theek hai bhai, main yahin hoon 👋")
        active = False
        continue

    last_active_time = time.time()

    response = route_command(text)

    if response == "EXIT":
        speak("Theek hai bhai, Jarvis band ho raha hai. Bye 👋")
        break

    if response:
        speak(response)
        time.sleep(0.4)
