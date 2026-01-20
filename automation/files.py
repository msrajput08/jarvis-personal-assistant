import os
import subprocess

COMMON_FOLDERS = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
}

def open_folder(text):
    for name, path in COMMON_FOLDERS.items():
        if name in text:
            if os.path.exists(path):
                os.startfile(path)
                return f"{name} folder khol diya"
            else:
                return f"{name} folder nahi mila"
    return None


def open_file(text):
    # very basic example (can improve later)
    words = text.split()
    for word in words:
        if "." in word:  # looks like a file
            for folder in COMMON_FOLDERS.values():
                possible = os.path.join(folder, word)
                if os.path.exists(possible):
                    os.startfile(possible)
                    return f"{word} open kar diya"
    return None
