def detect_intent(text):
    text = text.lower()

    OPEN_WORDS = [
        "open", "start", "launch", "run",
        "khol", "chalu", "start karo", "open karo"
    ]

    CLOSE_WORDS = [
        "close", "band", "stop", "exit",
        "band karo", "close karo"
    ]

    SHUTDOWN_WORDS = ["shutdown", "power off", "off"]
    RESTART_WORDS = ["restart", "reboot"]

    if any(word in text for word in OPEN_WORDS):
        return "OPEN"

    if any(word in text for word in CLOSE_WORDS):
        return "CLOSE"

    if any(word in text for word in SHUTDOWN_WORDS):
        return "SHUTDOWN"

    if any(word in text for word in RESTART_WORDS):
        return "RESTART"

    return "UNKNOWN"
