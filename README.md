# 🤖 Jarvis – Personal AI Assistant

Jarvis is a Python-based personal AI assistant that supports voice and text interaction, system automation, and intelligent command handling.

It is designed as a learning-focused, extensible desktop assistant, inspired by real-world AI systems.

🚧 Status: Actively under development

---

## ✨ Features

### 🗣️ Voice & Text Interaction
- Voice-based interaction (Speech Recognition + Text-to-Speech)
- Text input via GUI
- Wake-word activation (Jarvis)
- Continuous conversation mode (no repeated wake word for 120 seconds)

### 🧠 Intelligent Command Handling
- Rule-based intent detection
- LLM fallback (OpenAI / Gemini) for unknown intents

### ⚙️ Automation & Actions
- Open / close applications
- Open folders & files
- System control (shutdown / restart)
- Weather updates using OpenWeather API
- WhatsApp automation (planned / optional)

### 🧱 Architecture
- Modular and clean architecture
- Separate files for routing, intent detection, automation, output, etc.

### 🔐 Secure API Key Handling
- API keys stored in .env
- .env ignored via .gitignore

---

## 🧩 Project Structure (Simplified)

jarvis/
├── main.py
├── config.py
├── voice_input.py
├── intent.py
├── router.py
├── output.py
├── automation/
│ ├── init.py
│ ├── system.py
│ ├── files.py
│ └── extras.py
├── llm.py
├── gui.py
├── requirements.txt
├── .gitignore
└── data/
├── memory.json
└── ...

---

## 🔐 Environment Setup

API keys are never hardcoded.

Create a .env file in the project root with the following variables:

OPENAI_KEY=your_openai_api_key_here  
GEMINI_KEY=path_to_gemini_json_key  
OPENWEATHER_KEY=your_openweather_api_key  

Make sure .env is added to .gitignore.

---

## ▶️ How to Run

1. Install dependencies  
   pip install -r requirements.txt

2. Run the assistant  
   python main.py

---

## ⚙️ Supported Intents (So Far)

OPEN      → open chrome / open folder / open file  
CLOSE     → close notepad / close app  
SHUTDOWN  → shutdown system  
RESTART   → restart system  
EXIT      → exit / quit / close jarvis  
UNKNOWN   → fallback to LLM  

---

## 🧠 Roadmap

- Persistent memory (JSON / SQLite)
- Plugin-based skill system
- Improved intent classification
- Personality modes
- Offline command support
- Packaging as executable (.exe)

---

## 🤝 Contributing

This is a personal learning project.  
Suggestions, issues, and pull requests are welcome and appreciated.

---

## 👤 Author

Mohit Rajput  
GitHub: https://github.com/msrajput08
