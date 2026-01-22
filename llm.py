import os
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

load_dotenv()

# ---------- OPENAI ----------
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

# ---------- GEMINI ----------
genai_client = genai.Client(
    api_key=os.getenv("GEMINI_KEY")
)

# ---------- OPENAI CALL ----------
def ask_openai(prompt):
    try:
        res = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return None


# ---------- GEMINI CALL ----------
def ask_gemini(prompt):
    try:
        res = genai_client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return res.text.strip()
    except Exception as e:
        return None


# ---------- SMART ROUTER ----------
def ask_llm(prompt):   # 🔥 Name changed here
    """
    Pehle OpenAI try karega
    Agar fail hua toh Gemini fallback
    """
    answer = ask_openai(prompt)
    if answer:
        return answer

    answer = ask_gemini(prompt)
    if answer:
        return answer

    return "LLM se response nahi mil pa raha bhai 😕"
