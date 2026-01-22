from output import speak
from voice_input import get_voice_command, get_text_command

YES_WORDS = ["yes", "haan", "ha", "yep", "sure"]
NO_WORDS = ["no", "nah", "nahi", "na"]

def confirm_action(action_text):
    """
    Asks user to confirm an action (voice or text).
    Returns True if confirmed, False otherwise.
    """

    speak(f"Confirm karo bhai, kya main {action_text} karu? Yes ya No bolo")

    for _ in range(3):  # max 3 tries
        # Voice first
        ans = get_voice_command()
        if not ans:
            ans = get_text_command()

        if not ans:
            continue

        ans = ans.lower().strip()

        if any(word in ans for word in YES_WORDS):
            return True

        if any(word in ans for word in NO_WORDS):
            speak("Action cancel kar diya ✅")
            return False

        speak("Haan ya nahi bolo bhai")

    speak("Response nahi mila, action cancel kar diya ✅")
    return False
