import webbrowser
import datetime
import pyautogui
import time
import os
import math
import re
import requests

# -----------------------------
# Time
# -----------------------------
def get_time():
    now = datetime.datetime.now()
    return f"Abhi ka time {now.strftime('%I:%M %p')} hai"

# -----------------------------
# Web search
# -----------------------------
def web_search(text):
    query = text.replace("search", "").replace("google", "").strip()
    if not query:
        return "Kya search karna hai?"
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching {query}"

# -----------------------------
# YouTube play
# -----------------------------
def play_youtube(text):
    query = text.replace("youtube", "").replace("play", "").strip()
    if not query:
        return "Kaunsa gaana ya video play karna hai?"
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Playing {query} on YouTube"

# -----------------------------
# Open websites
# -----------------------------
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com"
}

def open_website(text):
    for name, url in WEBSITES.items():
        if name in text:
            webbrowser.open(url)
            return f"{name} open kar diya"
    return "Kaunsa website open karna hai?"

# -----------------------------
# Reminder
# -----------------------------
def set_reminder(text):
    # Example: remind me in 10 minutes to drink water
    match = re.search(r"in (\d+) (minute|minutes|hour|hours) to (.+)", text)
    if not match:
        return "Reminder format: remind me in 10 minutes to drink water"

    value = int(match.group(1))
    unit = match.group(2)
    message = match.group(3)

    seconds = value * 60 if "minute" in unit else value * 3600
    time.sleep(seconds)

    return f"Reminder: {message}"

# -----------------------------
# Screenshot
# -----------------------------
def take_screenshot():
    path = os.path.join(os.path.expanduser("~"), "Desktop", "screenshot.png")
    image = pyautogui.screenshot()
    image.save(path)
    return f"Screenshot save kar diya Desktop me: screenshot.png"

# -----------------------------
# Calculator
# -----------------------------
def calculate(text):
    try:
        # Remove non math characters
        expr = re.sub(r"[^0-9\+\-\*\/\.\(\) ]", "", text)
        result = eval(expr)
        return f"Answer: {result}"
    except:
        return "Calculation samajh nahi aayi. Example: calculate 5 + 7"

# -----------------------------
# Weather (OpenWeather API)
# -----------------------------
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

def get_weather(text):
    # Example inputs:
    # "weather in delhi"
    # "temperature mumbai"
    # "weather delhi"
    # "weather"

    if not OPENWEATHER_KEY:
        return "Weather key missing. .env me OPENWEATHER_KEY add karo."

    # Clean input
    text = text.lower().strip()

    # Remove trigger words
    for word in ["weather", "temperature", "temp", "mausam"]:
        text = text.replace(word, "")

    # Handle "in" keyword
    text = text.replace("in", " ").strip()

    city = text.strip()
    if not city:
        return "Kis city ka weather chahiye? (Example: 'jarvis weather in delhi')"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"

    try:
        res = requests.get(url).json()

        # API error handling
        if res.get("cod") != 200:
            return "City nahi mili ya API error. City name check karo."

        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]

        return f"{city.title()} ka weather {desc} hai aur temperature {temp}°C hai."

    except Exception as e:
        print("Weather Error:", e)
        return "Weather info nahi mil pa rahi. Check your internet connection."
