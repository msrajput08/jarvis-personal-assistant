from output import speak
from voice_input import get_voice_command
from voice_input import get_text_command

def confirm_action(action_text):
    """
    Asks user to confirm an action (voice or text)
    Returns True if user confirms, False otherwise
    """

    speak(f"Are you sure you want to {action_text}? Please say yes or no")

    for _ in range(3):  # 3 tries
        # try voice first
        ans = get_voice_command()
        if not ans:
            ans = get_text_command()

        ans = ans.lower()
        if "yes" in ans:
            return True
        elif "no" in ans:
            speak("Action cancelled ✅")
            return False
        else:
            speak("Please say yes or no")

    speak("No valid response. Action cancelled ✅")
    return False
