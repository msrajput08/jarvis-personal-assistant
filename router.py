from intent import detect_intent
from automation.system import open_app, close_app, system_control
from automation.files import open_folder, open_file
from confirm import confirm_action  # import confirmation

def route_command(text):

    if any(x in text for x in ["hello", "hi"]):
        return "Hello bhai 👋"

    if "how are you" in text:
        return "Main badhiya hoon, kaam bata"

    intent = detect_intent(text)

    # DANGEROUS actions
    if intent in ["SHUTDOWN", "RESTART"]:
        if confirm_action(intent.lower()):
            return system_control(intent)
        else:
            return "Action cancelled"

    if intent == "CLOSE":
        # optionally confirm for apps
        if confirm_action("close app"):
            return close_app(text)
        else:
            return "Action cancelled"

    # FILE / FOLDER
    if intent == "OPEN":
        result = open_folder(text)
        if result:
            return result

        result = open_file(text)
        if result:
            return result

        return open_app(text)

    return "Samajh nahi aaya"
