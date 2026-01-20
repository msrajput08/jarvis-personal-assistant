import os
import pyautogui

APPS = {
    "chrome": ["chrome", "google chrome"],
    "notepad": ["notepad"],
    "calculator": ["calculator", "calc"],
    "code": ["vs code", "vscode", "code"],
    "explorer": ["explorer", "file manager"]
}

def open_app(text):
    for app, keywords in APPS.items():
        for word in keywords:
            if word in text:
                os.system(f"start {app}")
                return f"{app} khol diya"
    return "Kaunsa app kholna hai?"

def close_app(text):
    for app in APPS:
        if app in text:
            os.system(f"taskkill /f /im {app}.exe")
            return f"{app} band kar diya"
    return "Close karne layak app nahi"

def system_control(intent):
    if intent == "SHUTDOWN":
        os.system("shutdown /s /t 5")
        return "System shutdown ho raha hai"

    if intent == "RESTART":
        os.system("shutdown /r /t 5")
        return "System restart ho raha hai"

    return None
