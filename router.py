from intent import detect_intent
from automation.system import open_app, close_app, system_control
from automation.files import open_folder, open_file
from automation.extra import (
    get_time, web_search, play_youtube, open_website,
    set_reminder, take_screenshot, calculate, get_weather
)
from confirm import confirm_action
from llm import ask_llm


def route_command(text):
    text = text.lower().strip()

    if any(x in text for x in ["hello", "hi", "hey", "namaste"]):
        return "Hello bhai 👋"

    if "how are you" in text:
        return "Main badhiya hoon 😎"

    intent = detect_intent(text)

    if intent == "EXIT":
        return "EXIT"

    if intent == "TIME":
        return get_time()

    if intent == "SEARCH":
        return web_search(text)

    if intent == "YOUTUBE":
        return play_youtube(text)

    if intent == "WEBSITE":
        return open_website(text)

    if intent == "REMINDER":
        return set_reminder(text)

    if intent == "SCREENSHOT":
        return take_screenshot()

    if intent == "CALCULATE":
        return calculate(text)

    if intent == "WEATHER":
        return get_weather(text)

    if intent in ["SHUTDOWN", "RESTART"]:
        if confirm_action(intent.lower()):
            return system_control(intent)
        return "Action cancel kar diya bhai 👍"

    if intent == "CLOSE":
        if confirm_action("close app"):
            return close_app(text)
        return "Action cancel kar diya"

    if intent == "OPEN":
        return open_folder(text) or open_file(text) or open_app(text)

    return ask_llm(text)
