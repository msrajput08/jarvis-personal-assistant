def detect_intent(text):
    text = text.lower().strip()

    INTENTS = {
        "EXIT": ["exit", "quit", "bye", "stop", "close jarvis"],
        "OPEN": ["open", "start", "launch", "run", "khol", "chalu", "start karo", "open karo"],
        "CLOSE": ["close app", "band karo", "close karo", "band", "stop", "exit"],
        "SHUTDOWN": ["shutdown", "power off", "off"],
        "RESTART": ["restart", "reboot"],
        "TIME": ["time", "kya time", "samay"],
        "SEARCH": ["search", "google", "find"],
        "YOUTUBE": ["youtube", "play on youtube", "play youtube"],
        "WEBSITE": ["open website", "open site", "open google", "open youtube", "open github"],
        "REMINDER": ["remind me", "reminder", "set reminder"],
        "SCREENSHOT": ["screenshot", "take screenshot"],
        "CALCULATE": ["calculate", "what is", "solve"],
        "WHATSAPP": ["whatsapp", "send message", "message on whatsapp"],
        "WEATHER": ["weather", "temperature", "forecast"]
    }

    for intent, keywords in INTENTS.items():
        for word in keywords:
            if word in text:
                return intent

    return "UNKNOWN"
