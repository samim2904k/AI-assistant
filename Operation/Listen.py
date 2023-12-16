import speech_recognition as sr
from googletrans import Translator

def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio , language="en")
            return query
        except:
            print("Sorry couldn't understand that ... please repeat ..")
    
def translationHindiToEnglish(text):
    line = str(text)
    result = Translator().translate(line)
    data = result.text
    return data

def Enzo_fun():
    query=Listen()
    text=translationHindiToEnglish(query)
    return text

# Enzo_fun()