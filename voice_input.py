import speech_recognition as sr

r = sr.Recognizer()

def get_voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""
    
def get_text_command():
    return input("You: ").lower()
