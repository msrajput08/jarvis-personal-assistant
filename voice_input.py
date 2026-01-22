import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.6
r.energy_threshold = 250

def get_voice_command(timeout=4):
    try:
        mic = sr.Microphone()  # no device_index
        with mic as source:
            print("🎙 Listening (voice)...")
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=4)
    except sr.WaitTimeoutError:
        print("⏰ Voice timeout")
        return ""
    except Exception as e:
        print("❌ Mic error:", e)
        return ""

    try:
        text = r.recognize_google(audio)
        print("🎤 RAW:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("🤷 Could not understand voice")
        return ""
    except sr.RequestError as e:
        print("❌ API error:", e)
        return ""



def get_text_command():
    try:
        return input("📝 You (text): ").lower().strip()
    except:
        return ""
