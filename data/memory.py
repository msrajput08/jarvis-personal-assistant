import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_value(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)

def get_value(key, default=None):
    return load_memory().get(key, default)
