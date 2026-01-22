import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 170)

_is_speaking = False


def speak(text):
    global _is_speaking
    if not text:
        return

    _is_speaking = True
    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()

    _is_speaking = False
    time.sleep(0.1)  # small buffer


def speaking():
    return _is_speaking
