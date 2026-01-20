# Jarvis – Personal AI Assistant 🤖

Jarvis is a **Python-based personal AI assistant** that supports **voice and text interaction**, system automation, and intelligent command handling.

It is designed as a **learning-focused, extensible desktop assistant**, inspired by real-world AI systems.

> 🚧 This project is actively under development.

---

## ✨ Features

- 🗣️ Voice-based interaction (Speech Recognition + TTS)
- 💬 Text input via GUI
- 🎯 Wake-word activation (`Jarvis`)
- 🔁 Continuous conversation mode (no repeated wake word)
- 🧠 Intent detection with LLM fallback
- ⚙️ System & browser automation
- 🧱 Modular and clean architecture
- 🔐 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

- Python 3
- SpeechRecognition
- pyttsx3
- Tkinter (GUI)
- OpenAI / Gemini (optional LLM integration)
- Git & GitHub

---

## 📂 Project Structure (Simplified)

jarvis/
├── main.py
├── config.py
├── voice.py
├── intent.py
├── automation.py
├── llm.py
├── gui.py
├── requirements.txt
├── .gitignore
└── data/

yaml
Copy code

---

## 🔐 Environment Setup

API keys are **not hardcoded**.

Create a `.env` file in the project root:

OPENAI_API_KEY=your_openai_api_key_here
GEMINI_KEY_PATH=path_to_gemini_json_key

yaml
Copy code

Make sure `.env` is added to `.gitignore`.

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
Requirements
Microphone (for voice mode)

Internet connection (for LLM features)

⚠️ Known Limitations
Memory system is basic (no long-term memory yet)

Intent detection is rule-based

Limited built-in skills

Windows-focused automation

🗺️ Roadmap
Persistent memory (JSON / SQLite)

Plugin-based skill system

Better intent classification

Personality modes

Offline command support

Packaging as executable (.exe)

🤝 Contributing
This is a personal learning project.
Suggestions, issues, and pull requests are welcome.

👤 Author
Mohit Rajput
GitHub: https://github.com/msrajput08
